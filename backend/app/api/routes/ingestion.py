"""Ingestion API routes."""

from app.db.session import get_db
from app.schemas.ingestion import ingestion_run
from app.services.queries.ingestion_service import get_ingestion_run
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/ingestion-runs", response_model=list[ingestion_run])
def read_ingestion_runs(db: Session = Depends(get_db)):
    return get_ingestion_run(db)
