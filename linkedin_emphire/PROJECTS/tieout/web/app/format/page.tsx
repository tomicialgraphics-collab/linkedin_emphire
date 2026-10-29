import type { Metadata } from "next";
import { DocsPage } from "../../components/DocsPage";

export const metadata: Metadata = {
  title: "bundle format v1",
  description: "the record schema, the chain, the gap codes, the verify procedure",
};

export default function FormatPage() {
  return <DocsPage docKey="format" />;
}
