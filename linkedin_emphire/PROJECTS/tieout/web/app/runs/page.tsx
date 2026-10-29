import type { Metadata } from "next";
import { RunList } from "../../components/RunList";

export const metadata: Metadata = { title: "runs" };

export default function RunsPage() {
  return <RunList />;
}
