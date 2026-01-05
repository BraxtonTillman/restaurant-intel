# Restaurant Intelligence Tool — Margin Leak Detector

A decision-first tool for independent restaurant owners. Ingests sales + purchase data (Toast exports now, Toast API later) and produces a weekly ranked list of margin leaks with recommended actions.

## What it does (V1)

- Upload CSV exports (sales + purchases + optional recipes/prices)
- Compute expected vs actual cost (starting with reasonable approximations)
- Detect & rank “leaks” (variance x volume)
- Output an opinionated “Top Leaks This Week” list (not a wall of reports)

## Tech stack

- Backend: FastAPI + PostgreSQL + SQLAlchemy + Alembic
- Frontend: Next.js + Tailwind + shadcn/ui (optional)
- Deploy: API (Render/Railway), Web (Vercel), DB (Supabase Postgres)

## Local dev

### Prereqs

- Docker + Docker Compose
- Python 3.11+
- Node 18+ (or 20)

### Start everything with Docker

```bash
docker compose up --build
