import type { Metadata } from "next";
import { FamiliesIndex } from "../../components/FamiliesIndex";

export const metadata: Metadata = { title: "families" };

export default function FamiliesPage() {
  return <FamiliesIndex />;
}
