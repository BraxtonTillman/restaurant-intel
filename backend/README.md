# Restaurant Intel — Backend (CRUD API)

This directory contains the FastAPI backend for a simple restaurant‑themed CRUD app.  
It exposes basic REST endpoints and talks to a PostgreSQL database.  
This is a learning project, not a production “intelligence platform.”

---

## What this backend does

- Defines a few database models (e.g. restaurant‑related entities).
- Exposes create/read/update/delete endpoints for those models.
- Uses SQLAlchemy + Alembic to manage the schema.
- Runs locally behind Docker or directly with Python.

---

## Run locally

**With Docker (recommended):** From the repo root, follow the main [README](../README.md) and run:

```bash
make dev
```

The backend will be available at <http://localhost:8000>.

**Without Docker:** From this directory, with Python and [uv](https://docs.astral.sh/uv/) installed:

```bash
uv sync
uv run uvicorn app.main:app --reload
```

Make sure `DATABASE_URL` and other env vars are set (see the root `.env.example`).

---

## Project layout (high level)

| Path           | Purpose                                  |
| -------------- | ---------------------------------------- |
| `app/api/`     | HTTP routes and API layer               |
| `app/db/`      | DB session, base, and Alembic config    |
| `app/models/`  | SQLAlchemy models                       |
| `app/schemas/` | Pydantic request/response schemas       |
| `tests/`       | Backend tests (where present)           |

---

## Helpful commands

From the repo root:

- `make backend-test` — run backend tests  
- `make backend-lint` — lint backend code  
- `make backend-fmt` — format backend code  

From this directory:

- `uv run pytest` — run tests  
- `uv run ruff check .` — lint  
- `uv run ruff format .` — format  
- `uv run alembic upgrade head` — apply DB migrations (requires `DATABASE_URL`)  

For more context about the overall app, see the [root README](../README.md).
