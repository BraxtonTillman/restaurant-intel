"""CLI entrypoint to recompute daily sales metrics from sales_orders."""

from app.services.metrics.compute_daily import compute_daily_metrics


def main() -> None:
    """Run the daily metrics computation and persist results to metrics_daily."""
    compute_daily_metrics()


if __name__ == "__main__":
    main()
