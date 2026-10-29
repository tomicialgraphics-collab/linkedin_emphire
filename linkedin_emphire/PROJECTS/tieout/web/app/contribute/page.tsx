import type { Metadata } from "next";
import { DocsPage } from "../../components/DocsPage";

export const metadata: Metadata = {
  title: "contributing",
  description: "how to add a family, a run, or a check, with the rules the code enforces",
};

export default function ContributePage() {
  return <DocsPage docKey="contributing" />;
}
