const SERVER_API_BASE_URL = "http://backend:8000";
const BROWSER_API_BASE_URL =
  process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

export async function getMetrics() {
  const isServer = typeof window === "undefined";
  const baseUrl = isServer ? SERVER_API_BASE_URL : BROWSER_API_BASE_URL;

  const res = await fetch(`${baseUrl}/metrics/summary`);

  if (!res.ok) {
    throw new Error(`Failed to fetch metrics: ${res.status} ${res.statusText}`);
  }

  return res.json();
}
