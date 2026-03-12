import "./globals.css";
import Link from "next/link";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "My Dashboard",
  description: "My metrics app",
};

const navLinkClass = "bg-blue-500 px-4 py-2 rounded mr-2 no-underline";

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <nav className="px-3 py-6 text-white">
          <Link className={navLinkClass} href="/">
            Home
          </Link>
          <Link className={navLinkClass} href="/metrics">
            Metrics
          </Link>
        </nav>
        <main className="px-8 py-6">{children}</main>
      </body>
    </html>
  );
}
