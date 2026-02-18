"""
Docstring for backend.app.services.metrics.compute_daily
"""

from datetime import date

from app.db.session import SessionLocal
from app.models.metrics import MetricsDaily
from app.models.sales import SalesOrder
from sqlalchemy import Date, cast, func, select


def compute_daily_metrics():
    db = SessionLocal()
    try:
        # Group sales_orders by calendar date (occurred_at), sum total, count orders
        stmt = (
            select(
                cast(SalesOrder.occurred_at, Date).label("date"),
                func.coalesce(func.sum(SalesOrder.total), 0).label("sales_total"),
                func.count().label("order_count"),
            )
            .group_by(cast(SalesOrder.occurred_at, Date))
        )
        rows = db.execute(stmt).all()

        # Upsert into metrics_daily (idempotent: re-run updates, does not duplicate)
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
