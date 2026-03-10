import { getMetrics } from "@/lib/api";

const cardClass = "bg-white rounded-xl shadow p-8 gap-4";

export default async function Metrics() {
  const metrics = await getMetrics();
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
    </div>
  );
}
