from app.api.routes.ingestion import router as ingestion_runs
from app.api.routes.metrics import router as metrics_summary
from fastapi import FastAPI

app = FastAPI()
app.include_router(metrics_summary)
app.include_router(ingestion_runs)


@app.get("/")
def root():
    return {"message": "Hello, World!"}

