"""Ingestion Pydantic schemas."""

from datetime import datetime

from pydantic import BaseModel

from app.models.sales import IngestionStatus


class SalesOrderSchema(BaseModel):
    id: int
    order_id: str
    occurred_at: datetime
    total: float
    created_at: datetime

    model_config = {"from_attributes": True}


class IngestionRun(BaseModel):
    id: int
    source: str
    status: IngestionStatus
    file_path: str
    created_at: datetime
    updated_at: datetime
    sales_orders: list[SalesOrderSchema]

    model_config = {"from_attributes": True}
