from fastapi import FastAPI

from app.api.routes.ingestion import router as ingestion_runs
from app.api.routes.metrics import router as metrics_summary
from app.api.routes.upload import router as upload_csv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(metrics_summary)
app.include_router(ingestion_runs)
app.include_router(upload_csv)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Hello, World!"}
