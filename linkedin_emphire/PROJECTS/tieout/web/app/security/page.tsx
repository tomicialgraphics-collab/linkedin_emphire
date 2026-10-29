import type { Metadata } from "next";
import { DocsPage } from "../../components/DocsPage";

export const metadata: Metadata = {
  title: "security",
  description: "scope, verify-don't-trust, disclosure",
};

export default function SecurityPage() {
  return <DocsPage docKey="security" />;
}
