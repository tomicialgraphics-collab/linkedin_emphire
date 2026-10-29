import type { Metadata } from "next";
import { ReproPage } from "../../components/ReproPage";

export const metadata: Metadata = {
  title: "reproduce",
  description: "the exact commands and expected output for every committed run",
};

export default function ReproRoute() {
  return <ReproPage />;
}
