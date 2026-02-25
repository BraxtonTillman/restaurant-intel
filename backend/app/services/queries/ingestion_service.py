"""Ingestion service queries."""

from app.models.metrics import MetricsDaily
from sqlalchemy.orm import Session


def get_daily_metrics(db: Session):
    return db.query(MetricsDaily).all()
