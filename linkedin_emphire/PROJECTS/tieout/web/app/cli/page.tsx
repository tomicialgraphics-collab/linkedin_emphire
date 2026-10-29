import type { Metadata } from "next";
import { CliPage } from "../../components/CliPage";

export const metadata: Metadata = {
  title: "cli",
  description: "every tieout command and flag, as the parser defines them",
};

export default function CliRoute() {
  return <CliPage />;
}
