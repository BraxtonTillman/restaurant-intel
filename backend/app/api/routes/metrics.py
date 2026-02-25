"""Metrics API routes."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.metrics import metrics_daily
from app.services.queries.metrics_service import get_daily_metrics

router = APIRouter()


@router.get("/metrics/summary", response_model=list[metrics_daily])
def read_metrics(db: Session = Depends(get_db)):
    return get_daily_metrics(db)
