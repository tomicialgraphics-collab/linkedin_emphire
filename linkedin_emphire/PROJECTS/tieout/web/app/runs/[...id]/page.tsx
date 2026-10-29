import type { Metadata } from "next";
import { RunDetail } from "../../../components/RunDetail";

// The committed evidence runs. Add an entry when a new run is committed.
const RUNS: string[][] = [
  ["demo"],
  ["demo-f2"],
  ["demo-stability", "a"],
  ["demo-stability", "b"],
];

export function generateStaticParams() {
  return RUNS.map((id) => ({ id }));
}

export const dynamicParams = false;

export function generateMetadata({ params }: { params: { id: string[] } }): Metadata {
  return { title: `run ${params.id.join("/")}` };
}

export default function RunDetailRoute({ params }: { params: { id: string[] } }) {
  return <RunDetail id={params.id.join("/")} />;
}
