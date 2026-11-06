#!/usr/bin/env node
// foray-probe.mjs - independent reproduction harness for the FORAY stream walk.
//
// Usage:
//   node foray-probe.mjs <path-to-verifier-folder>
//
// The folder must be a copy of the WP-1 verifier (the one containing lib/,
// vectors/, test/, foray-verifier.mjs). Nothing is fetched at run time and
// nothing outside the folder is read.
//
// Group A cases leave the bundle's header untouched, so the bundle stays
// internally valid and any change in outcome comes from the stream walk alone.
//
// Group B cases synthesise an anchored extent: they add a stream segment to
// header_echo, recompute the anchored value from the new header, and write
// the recomputed value into both canned chain sources so the anchor check
// still passes. Those cases are labelled SYNTHETIC in the output because the
// vector pack contains no shipped vector that carries both a stream_context
// and a populated segment extent.
//
// Output is one line per case: id, outcome, failed check, reason.
// Exit code 0 if the probe ran, regardless of the outcomes it measured.
// Exit code 2 if the folder does not look like a verifier.

import { pathToFileURL } from 'node:url';
import { createHash } from 'node:crypto';
import path from 'node:path';
import fs from 'node:fs';

const root = process.argv[2];
if (!root) {
  console.error('usage: node foray-probe.mjs <path-to-verifier-folder>');
  process.exit(2);
}

const abs = path.resolve(root);
const need = ['lib/checks.mjs', 'lib/context-io.mjs', 'lib/abh.mjs', 'vectors'];
const missing = need.filter((p) => !fs.existsSync(path.join(abs, p)));
if (missing.length) {
  console.error(`not a verifier folder: ${abs}`);
  console.error(`missing: ${missing.join(', ')}`);
  process.exit(2);
}

const checks = await import(pathToFileURL(path.join(abs, 'lib/checks.mjs')).href);
const contextIo = await import(pathToFileURL(path.join(abs, 'lib/context-io.mjs')).href);
const abh = await import(pathToFileURL(path.join(abs, 'lib/abh.mjs')).href);
const bundleIo = await import(pathToFileURL(path.join(abs, 'lib/bundle.mjs')).href);

const loadVector = (kind, name) =>
  JSON.parse(fs.readFileSync(path.join(abs, 'vectors', kind, `${name}.json`), 'utf8'));

const clone = (x) => JSON.parse(JSON.stringify(x));
const h = (s) => createHash('sha256').update(s).digest('hex');

function chain(from, to, salt, opts = {}) {
  const out = [];
  let prev = h(`${salt}|before|${from}`);
  for (let seq = from; seq <= to; seq++) {
    let txHash = h(`${salt}|${seq}`);
    if (seq === from && opts.firstHash) txHash = opts.firstHash;
    if (seq === to && opts.lastHash) txHash = opts.lastHash;
    out.push({ seqNo: seq, txHash, prevTxHash: prev, anchoredAt: 1783941000, chainId: 'kaspa-mainnet' });
    prev = txHash;
  }
  return out;
}

function bySeq(history) {
  return [...history].sort((a, b) => a.seqNo - b.seqNo);
}

async function run(label, bundle, rawContext) {
  const context = contextIo.deserializeContext(clone(rawContext));
  let line;
  try {
    const result = await checks.verify(clone(bundle), context);
    const check = String(result.failedCheck ?? '-');
    line = `${label.padEnd(46)} ${String(result.outcome).padEnd(20)} check=${check.padEnd(3)} ${result.reason ?? ''}`;
  } catch (err) {
    line = `${label.padEnd(46)} THREW              ${err?.message ?? err}`;
  }
  console.log(line);
  return line;
}

const results = [];
const record = async (label, bundle, ctx) => results.push(await run(label, bundle, ctx));

// ---------------------------------------------------------------- group A
// History-only mutations. The header is untouched, so the anchor still matches.

for (const [vector, short] of [
  ['positive/rotated-chain-seam', 'rotated-chain-seam'],
  ['negative/N10-backdated-insert-fork', 'N10'],
]) {
  const v = loadVector(vector.split('/')[0], vector.split('/')[1]);
  const base = v.bundle;
  const ctx = v.context;
  const hist = bySeq(ctx.streamHistory);

  await record(`${short}: as shipped`, base, ctx);
  await record(`${short}: tail record removed`, base, { ...ctx, streamHistory: hist.slice(0, -1) });
  await record(`${short}: head record removed`, base, { ...ctx, streamHistory: hist.slice(1) });
  await record(`${short}: history emptied`, base, { ...ctx, streamHistory: [] });

  const falsified = clone(base);
  falsified.stream_context.prev_tx_hash = '00'.repeat(32);
  await record(`${short}: declared prev_tx_hash falsified`, falsified, ctx);
}

// ---------------------------------------------------------------- group B
// SYNTHETIC: a bundle carrying both a stream_context and an anchored extent.
// The shipped packet has no vector that carries both, which is why these
// cases exist: without an anchored extent there is nothing for a walk to be
// short of.

{
  const v = loadVector('positive', 'rotated-chain-seam');
  const declaredPrev = v.bundle.stream_context.prev_tx_hash;
  const realHead = h('probe|head|412');

  const makeBundle = (segHeadHash) => {
    const bundle = clone(v.bundle);
    bundle.header_echo.stream_segments = [
      {
        stream_id: 'aa'.repeat(16),
        first_seq: '0',
        last_seq: '412',
        head_hash: segHeadHash,
      },
    ];
    const anchored = Buffer.from(
      abh.computeAnchoredValue(bundleIo.headerEchoToBatchHeader(bundle.header_echo))
    ).toString('hex');
    const ctx = clone(v.context);
    for (const src of ctx.chainSources) {
      for (const id of Object.keys(src.canned)) {
        src.canned[id].anchoredValue = anchored;
      }
    }
    return { bundle, ctx };
  };

  const good = makeBundle(realHead);
  const badHead = makeBundle(h('probe|head|wrong'));

  const complete = chain(0, 412, 'full', { firstHash: declaredPrev, lastHash: realHead });
  const tailShort = chain(0, 400, 'tail', { firstHash: declaredPrev });
  const headShort = chain(300, 412, 'head', { lastHash: realHead });
  const single = [headShort[headShort.length - 1]];

  await record('SYNTH extent 0..412, history 0..412, head matches', good.bundle, {
    ...good.ctx,
    streamHistory: complete,
  });
  await record('SYNTH extent 0..412, history 0..412, head falsified', badHead.bundle, {
    ...badHead.ctx,
    streamHistory: complete,
  });
  await record('SYNTH extent 0..412, history 0..400', good.bundle, { ...good.ctx, streamHistory: tailShort });
  await record('SYNTH extent 0..412, history 300..412', good.bundle, { ...good.ctx, streamHistory: headShort });
  await record('SYNTH extent 0..412, history [412]', good.bundle, { ...good.ctx, streamHistory: single });
  await record('SYNTH extent 0..412, history []', good.bundle, { ...good.ctx, streamHistory: [] });
}

console.log('');
console.log(`${results.length} cases run against ${abs}`);
console.log('Group A cases hold the bundle valid and vary only the history.');
console.log('Group B cases are synthetic: the vector pack ships no bundle with both a');
console.log('stream_context and a populated segment extent.');
