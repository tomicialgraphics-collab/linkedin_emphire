import type { Metadata } from "next";
import { DocsPage } from "../../components/DocsPage";

export const metadata: Metadata = {
  title: "method note",
  description: "the gap, the pillars as doctrine, how to read a bundle, reproducibility stated precisely",
};

export default function MethodPage() {
  return <DocsPage docKey="method" />;
}
