import type { Metadata } from "next";
import { DocsPage } from "../../components/DocsPage";

export const metadata: Metadata = {
  title: "license",
  description: "MIT",
};

export default function LicensePage() {
  return <DocsPage docKey="license" />;
}
