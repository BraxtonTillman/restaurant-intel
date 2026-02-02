# ---------- Base image ----------
FROM python:3.13-slim

# Prevent python from buffering stdout/stderr
ENV PYTHONUNBUFFERED=1

# System deps (for psycopg, builds, etc.)
RUN apt-get update && apt-get install -y \
  build-essential \
  curl \
  && rm -rf /var/lib/apt/lists/*

# ---------- Install uv ----------
RUN pip install --no-cache-dir uv

# ---------- Set workdir ----------
WORKDIR /app

ENV UV_SYSTEM_PYTHON=1

# ---------- Copy dependency files first (for caching) ----------
COPY pyproject.toml uv.lock* ./

# Install dependencies into the image
RUN uv sync --frozen

# ---------- Copy the rest of the app ----------
COPY . .

# ---------- Expose FastAPI port ----------
EXPOSE 8000

# ---------- Default command ----------
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
