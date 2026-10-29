import type { Metadata } from "next";
import { DocsPage } from "../../components/DocsPage";

export const metadata: Metadata = {
  title: "changelog",
  description: "all notable changes to tieout",
};

export default function ChangelogPage() {
  return <DocsPage docKey="changelog" />;
}
