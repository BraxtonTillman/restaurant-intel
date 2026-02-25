from app.api.routes.metrics import router as metrics_summary
from fastapi import FastAPI

app = FastAPI()
app.include_router(metrics_summary)

@app.get("/")
def root():
    return {"message": "Hello, World!"}

