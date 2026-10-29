import type { Metadata } from "next";
import { FamilyDetail } from "../../../components/FamilyDetail";

// Live families. F3-F6 are planned against the OWASP Agentic crosswalk
// and get pages here when they ship.
const FAMILIES = ["f1", "f2"];

export function generateStaticParams() {
  return FAMILIES.map((familyId) => ({ familyId }));
}

export const dynamicParams = false;

export function generateMetadata({ params }: { params: { familyId: string } }): Metadata {
  return { title: `family ${params.familyId.toUpperCase()}` };
}

export default function FamilyPage({ params }: { params: { familyId: string } }) {
  return <FamilyDetail id={params.familyId.toUpperCase()} />;
}
