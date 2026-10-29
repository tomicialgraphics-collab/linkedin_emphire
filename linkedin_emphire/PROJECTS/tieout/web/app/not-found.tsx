export default function NotFound() {
  return (
    <section>
      <div className="empty">
        404 · no bundle at this path
        <pre className="code">{`the record is either at a real run id under /runs,
or it does not exist. both are verifiable.`}</pre>
      </div>
      <p style={{ textAlign: "center" }}>
        <a className="back" href="/">
          ← home
        </a>
      </p>
    </section>
  );
}
