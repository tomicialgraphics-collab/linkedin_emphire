import type { Metadata } from "next";
import { DocsPage } from "../../components/DocsPage";

export const metadata: Metadata = {
  title: "harness spec",
  description: "the T0-T6 phases as implemented, tests A-D, the binding field map, the standing named gaps",
};

export default function HarnessPage() {
  return <DocsPage docKey="harness" />;
}
