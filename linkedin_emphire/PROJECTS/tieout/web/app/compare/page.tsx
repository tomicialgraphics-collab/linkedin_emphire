import type { Metadata } from "next";
import { Compare } from "../../components/Compare";

export const metadata: Metadata = { title: "compare" };

export default function ComparePage() {
  return <Compare />;
}
