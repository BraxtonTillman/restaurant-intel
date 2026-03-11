import { getMetrics, getIngestionRuns } from "@/lib/api";
import DeleteButton from "@/components/DeleteButton";

const cardClass = "bg-white rounded-xl shadow p-8 gap-4";

export default async function Metrics() {
  const metrics = await getMetrics();
  const ingestionRuns = await getIngestionRuns();
  return (
    <div>
      <h1 className="text-2xl font-bold p-8">Daily Metrics</h1>
      <div className={"grid grid-cols-3 gap-4"}>
        {metrics.map((item) => (
          <div className={cardClass} key={item.date}>
            <p className="font-bold">Date: {item.date}</p>
            <p className="text-green-600">Total Sales: {item.sales_total}</p>
            <p>Total Orders: {item.order_count}</p>
          </div>
        ))}
      </div>
      <h1 className="text-2xl font-bold p-8">Ingestion Runs</h1>
      <div className={"grid grid-cols-3 gap-4"}>
        {ingestionRuns.map((item) => (
          <div className={cardClass} key={item.id}>
            <p>ID: {item.id}</p>
            <p>Status: {item.status}</p>
            <p>Created: {item.created_at}</p>
            <p>Updated: {item.updated_at}</p>
            <DeleteButton id={item.id} />
          </div>
        ))}
      </div>
    </div>
  );
}
