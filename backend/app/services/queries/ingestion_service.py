'''Ingestion service query'''
from app.models.sales import IngestionRun
from sqlalchemy.orm import Session


def get_ingestion_run(db: Session):
    return db.query(IngestionRun).all()
