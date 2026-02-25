from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health():
    return {"ok": True}


@app.get("/")
def root():
    return {"message": "Hello, World!"}


@app.get("/metrics/summary")
def get_metrics_summary():
    pass
