export async function getMetrics() {
  const res = await fetch("http://localhost:8000/metrics/summary");
  return res.json();
}
