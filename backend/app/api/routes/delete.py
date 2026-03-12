from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.queries.ingestion_service import delete_ingestion_run as get_run_by_id

router = APIRouter()


@router.delete("/ingestion-runs/{id}")
def delete_ingestion_run(id: int, db: Session = Depends(get_db)):  # noqa: B008
    run = get_run_by_id(id, db)
    if run is None:
        raise HTTPException(status_code=404, detail="Not found")
    db.delete(run)
    db.commit()
    return {"message": "success"}