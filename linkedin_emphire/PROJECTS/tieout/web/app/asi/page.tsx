import type { Metadata } from "next";
import { AsiPage } from "../../components/AsiPage";

export const metadata: Metadata = {
  title: "owasp agentic crosswalk",
  description: "record-derived mapping of tieout checks to OWASP Agentic AI Threats ASI01-ASI10",
};

export default function AsiRoute() {
  return <AsiPage />;
}
