"""
Docstring for backend.app.models.metrics
"""
from datetime import date

from app.db.base import Base
from sqlalchemy import Date, Float, Integer
from sqlalchemy.orm import Mapped, mapped_column


class MetricsDaily(Base):
    __tablename__ = "metrics_daily"

    date: Mapped[date] = mapped_column(Date, primary_key=True)
    sales_total: Mapped[float] = mapped_column(Float)
    order_count: Mapped[int] = mapped_column(Integer)

    def __repr__(self) -> str:
        return f"<MetricsDaily(date={self.date}, sales_total={self.sales_total}, order_count={self.order_count})>"
