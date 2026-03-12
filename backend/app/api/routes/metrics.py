"""Metrics API routes."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.metrics import MetricsDaily
from app.services.queries.metrics_service import get_daily_metrics

router = APIRouter()


@router.get("/metrics/summary", response_model=list[MetricsDaily])
def read_metrics(db: Session = Depends(get_db)):  # noqa: B008
    return get_daily_metrics(db)
