const SERVER_API_BASE_URL = "http://backend:8000";
const BROWSER_API_BASE_URL =
  process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

export async function getMetrics() {
  const isServer = typeof window === "undefined";
  const baseUrl = isServer ? SERVER_API_BASE_URL : BROWSER_API_BASE_URL;

  try {
    const res = await fetch(`${baseUrl}/metrics/summary`);

    if (!res.ok) {
      console.error(
        `Failed to fetch metrics. Returning empty array. Status: ${res.status} ${res.statusText}`,
      );
      return [];
    }

    return await res.json();
  } catch (error) {
    console.error("Failed to fetch metrics. Returning empty array.", error);
    return [];
  }
}

export async function uploadCSV(file: File) {
  const formData = new FormData();
  formData.append("file", file);

  const res = await fetch(`${BROWSER_API_BASE_URL}/upload`, {
    method: "POST",
    body: formData,
  });

  if (!res.ok) {
    throw new Error(`Upload failed: ${res.status} ${res.statusText}`);
  }

  return res.json();
}

export async function deleteIngestion(id: number) {
  const res = await fetch(`${BROWSER_API_BASE_URL}/ingestion-runs/${id}`, {
    method: "DELETE",
  });

  if (!res.ok) {
    throw new Error(`Delete failed: ${res.status} ${res.statusText}`);
  }
  return res.json();
}

export async function getIngestionRuns() {
  const isServer = typeof window === "undefined";
  const baseUrl = isServer ? SERVER_API_BASE_URL : BROWSER_API_BASE_URL;

  try {
    const res = await fetch(`${baseUrl}/ingestion-runs`);

    if (!res.ok) {
      console.error(
        `Failed to fetch ingestion runs. Returning empty array. Status: ${res.status} ${res.statusText}`,
      );
      return [];
    }

    return await res.json();
  } catch (error) {
    console.error(
      "Failed to fetch ingestion runs. Returning empty array.",
      error,
    );
    return [];
  }
}
