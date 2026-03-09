import { getMetrics } from "@/lib/api";

export default async function Metrics() {
  const metrics = await getMetrics();
  return <div>{JSON.stringify(metrics)}</div>;
}
