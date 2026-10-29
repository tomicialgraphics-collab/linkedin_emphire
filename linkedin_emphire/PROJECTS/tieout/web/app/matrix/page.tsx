import type { Metadata } from "next";
import { DocsPage } from "../../components/DocsPage";

export const metadata: Metadata = {
  title: "failure-mode matrix",
  description: "four failure modes of decision-time evidence, five columns, two test classes",
};

export default function MatrixPage() {
  return <DocsPage docKey="matrix" />;
}
