"""Ingestion service queries."""

from sqlalchemy.orm import Session

from app.models.metrics import MetricsDaily


def get_daily_metrics(db: Session):
    return db.query(MetricsDaily).all()
