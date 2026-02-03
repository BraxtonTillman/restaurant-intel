FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1
ENV UV_SYSTEM_PYTHON=1

RUN apt-get update && apt-get install -y \
  build-essential \
  curl \
  && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir uv

WORKDIR /app

# Copy dependency files
COPY pyproject.toml uv.lock* ./

# Install dependencies
RUN uv sync --frozen

# Copy rest of app
COPY . .

EXPOSE 8000
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
