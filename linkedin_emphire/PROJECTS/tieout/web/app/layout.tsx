import type { Metadata } from "next";
import "./globals.css";
import { Shell } from "../components/Shell";

export const metadata: Metadata = {
  title: {
    default: "tieout: evidence-grade agent evaluation",
    template: "%s · tieout",
  },
  description:
    "An open harness for agent evaluation and red team runs that emits evidence, not reports. Every verdict is a bound, chained, re-derivable event.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <Shell>{children}</Shell>
      </body>
    </html>
  );
}
