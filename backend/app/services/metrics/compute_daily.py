"""Daily metrics computation: aggregate sales_orders by date and upsert into metrics_daily."""

from sqlalchemy import Date, cast, func, select

from app.db.session import SessionLocal
from app.models.metrics import MetricsDaily
from app.models.sales import SalesOrder


def compute_daily_metrics() -> None:
    """
    Recompute daily sales_total and order_count from sales_orders and upsert into metrics_daily.
    Idempotent: re-running overwrites existing rows for each date without duplicating.
    """
    db = SessionLocal()
    try:
        stmt = select(
            cast(SalesOrder.occurred_at, Date).label("date"),
            func.coalesce(func.sum(SalesOrder.total), 0).label("sales_total"),
            func.count().label("order_count"),
        ).group_by(cast(SalesOrder.occurred_at, Date))
        rows = db.execute(stmt).all()

        for row in rows:
            metrics = MetricsDaily(
                date=row.date,
                sales_total=row.sales_total,
                order_count=row.order_count,
            )
            db.merge(metrics)

        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
