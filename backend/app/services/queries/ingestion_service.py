"""Ingestion service query"""

from sqlalchemy.orm import Session

from app.models.sales import IngestionRun


def get_ingestion_run(db: Session):
    return db.query(IngestionRun).all()

def delete_ingestion_run(id: int, db: Session):
    return db.query(IngestionRun).filter(IngestionRun.id == id).first()
