from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.ingestion.ingest_csv import ingest_csv

router = APIRouter()


@router.post("/upload")
async def upload_csv(
    file: UploadFile = File(...), db: Session = Depends(get_db)
):  # noqa: B008
    contents = await file.read()
    ingest_csv(contents, db)
    return {"message": "success"}
