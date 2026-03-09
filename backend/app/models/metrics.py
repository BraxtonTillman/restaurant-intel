"""ORM models for precomputed metrics (e.g. daily rollups)."""

from datetime import date

from sqlalchemy import Date, Float, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class MetricsDaily(Base):
    """One row per calendar day: total sales and order count derived from sales_orders."""

    __tablename__ = "metrics_daily"

    date: Mapped[date] = mapped_column(Date, primary_key=True)
    sales_total: Mapped[float] = mapped_column(Float)
    order_count: Mapped[int] = mapped_column(Integer)

    def __repr__(self) -> str:
        return f"<MetricsDaily(date={self.date}, sales_total={self.sales_total}, order_count={self.order_count})>"
