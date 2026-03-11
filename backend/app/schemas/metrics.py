"""Pydantic schema for metrics"""

from datetime import date

from pydantic import BaseModel


class MetricsDaily(BaseModel):
    date: date
    sales_total: float
    order_count: int

    model_config = {"from_attributes": True}  # allows objects to be read
