# Restaurant Intel — Backend

FastAPI service that handles APIs, data ingestion, and business logic for the Restaurant Intelligence Platform. Runs alongside a background worker for scheduled jobs (e.g. ingestion, metrics).

## Run locally

**With Docker (recommended):** From the repo root, use the main [README](../README.md) setup. Start everything with:

```bash
make dev
```

The backend is then available at <http://localhost:8000>.

**Without Docker:** From this directory, with Python 3.13 and [uv](https://docs.astral.sh/uv/) installed:

```bash
uv sync
uv run uvicorn app.main:app --reload
```

Set `DATABASE_URL` and other env vars (see root `.env.example`) before running.

## Project layout

| Path | Purpose |
| ------ | --------- |
| `app/` | Application code |
| `app/api/` | HTTP routes and API layer |
| `app/db/` | Database session, base, and Alembic migrations |
| `app/models/` | SQLAlchemy models |
| `app/schemas/` | Pydantic request/response schemas |
| `app/services/` | Business logic (ingestion, storage, etc.) |
| `app/scripts/` | CLI scripts (e.g. ingest) |
| `app/workers/` | Background worker entrypoint |
| `tests/` | Pytest test suite |

## Commands

From repo root (preferred):

- `make backend-test` — run tests  
- `make backend-lint` — lint  
- `make backend-fmt` — format  

From this directory:

- `uv run pytest` — run tests  
- `uv run ruff check .` — lint  
- `uv run ruff format .` — format  
- `uv run alembic upgrade head` — run migrations (requires `DATABASE_URL`)  

For full setup and all commands, see the [root README](../README.md).
