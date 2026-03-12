from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.delete import router as delete_ingestion
from app.api.routes.ingestion import router as ingestion_runs
from app.api.routes.metrics import router as metrics_summary
from app.api.routes.upload import router as upload_csv

app = FastAPI()
app.include_router(metrics_summary)
app.include_router(ingestion_runs)
app.include_router(upload_csv)
app.include_router(delete_ingestion)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Hello, World!"}
