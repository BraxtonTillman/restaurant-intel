"""Ingestion API routes."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.ingestion import IngestionRun
from app.services.queries.ingestion_service import get_ingestion_run

router = APIRouter()


@router.get("/ingestion-runs", response_model=list[IngestionRun])
def read_ingestion_runs(db: Session = Depends(get_db)):  # noqa: B008
    return get_ingestion_run(db)
