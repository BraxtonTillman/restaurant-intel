# Restaurant Intel — Simple CRUD App

This repository contains one of my first full‑stack CRUD experiments.  
It is **not** a full “restaurant intelligence platform” or production SaaS product.  
Instead, it’s a learning project that lets you create, read, update, and delete basic restaurant‑related records through a small web UI and API.

---

## What it actually does

- **Basic CRUD**: simple create/read/update/delete operations for restaurant data (e.g. locations, menu items, or similar entities).
- **Web UI**: a small Next.js frontend for listing records and editing them.
- **API**: a FastAPI backend that exposes basic REST endpoints and talks to a PostgreSQL database.
- **Local only**: everything is intended to run on your machine for learning and experimentation.

There is no production deployment, no fancy analytics, and no real integrations here—just a straightforward CRUD app.

---

## Tech stack (kept simple)

- **Backend**: Python, FastAPI, SQLAlchemy, Alembic
- **Frontend**: Next.js (App Router), TypeScript, Tailwind CSS
- **Database**: PostgreSQL
- **Tooling**: Docker, Docker Compose, `make`

The code layout is split into a `backend` folder (API + database) and a `frontend` folder (UI).

---

## Running it locally

### Prerequisites

- Docker and Docker Compose
- `make`

### Setup

From your terminal:

```bash
git clone <repository-url>
cd restaurant-intel
cp .env.example .env
```

The default `.env` values are meant for local development.

### Start the app

From the repo root:

```bash
make dev
```

Once everything starts:

- **Frontend:** <http://localhost:3000>
- **Backend API / health:** <http://localhost:8000>

That’s enough to click around the UI and exercise basic CRUD against the database.

---

## Why this project exists

This codebase is mainly a place for me to practice:

- wiring up a real database behind a web app,
- handling simple REST endpoints,
- and seeing a full request go from the browser, through the API, into the database, and back.

If you’re reading this, treat it as a **learning sandbox**, not a polished product.
