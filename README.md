# Restaurant Intelligence Platform (MVP)

A local-first, data-driven SaaS platform designed to help restaurants identify margin leaks, understand operational performance, and make better decisions by aggregating data from existing systems such as POS, labor scheduling, and reservations.

This project is currently an MVP in active development. The primary focus is building a strong foundation: clean data ingestion, a canonical data model, reliable metrics, and actionable insights.

---

## Core Idea

Restaurants already collect a large amount of data, but it is fragmented across multiple tools. Interpreting that data and turning it into meaningful decisions is time-consuming and error-prone.

This platform acts as a decision layer on top of existing restaurant systems. It unifies data from multiple sources and translates it into clear metrics and recommendations, with the goal of improving margins and operational efficiency. The emphasis is on decision support rather than dashboards alone.

---

## Architecture Overview

This repository is structured as a monorepo and is intended to be run locally during development using Docker Compose. The architecture mirrors a production-ready setup while remaining simple enough for rapid iteration.

The system consists of the following components:

- A FastAPI backend responsible for APIs, data ingestion, and business logic
- A background worker process responsible for scheduled jobs such as ingestion and metric computation
- A Next.js frontend used to present metrics and insights
- A PostgreSQL database used as the canonical data store
- Docker Compose used to orchestrate local services

---

## Tech Stack

### Backend

- Python 3.12
- FastAPI
- SQLAlchemy and Alembic
- uv for dependency management

### Frontend

- Next.js (App Router)
- TypeScript
- Tailwind CSS
- pnpm

### Data and Jobs

- PostgreSQL 16
- Scheduled background worker (no message queue in MVP)
- Canonical schema with computed metrics

### Tooling

- Docker and Docker Compose
- GitHub Actions for CI
- Ruff, Pytest, ESLint

---

## Repository Structure

.
├── backend/ # FastAPI app, worker, database models, migrations
├── frontend/ # Next.js application
├── docs/ # Architecture and design notes
├── .github/ # CI workflows
├── docker-compose.yml
├── Makefile
├── .env.example
├── .editorconfig
└── .gitignore

---

## Local Development

### Prerequisites

- Docker and Docker Compose
- Make
- Node.js (optional, for running frontend outside Docker)

---

### Setup

Clone the repository and navigate into it:

```bash
git clone <repository-url>
cd restaurant-intelligence

Create a local environment file:

cp .env.example .env

The default values are suitable for local development.
Running the Application

Start all services:

make dev

This command starts the database, backend API, worker process, and frontend UI.

Access points:

    Frontend: http://localhost:3000

    Backend API: http://localhost:8000

    Health endpoint: http://localhost:8000/health

Common Development Commands

make backend-test     # Run backend test suite
make backend-lint     # Lint backend code
make backend-fmt      # Format backend code
make frontend-lint    # Lint frontend code
make frontend-build   # Build frontend
make docker-build     # Build Docker images (sanity check)
make logs             # Follow container logs
make down             # Stop all services

Run make with no arguments to see all available targets.
Continuous Integration

GitHub Actions runs on pull requests and on pushes to the main branch. The CI pipeline enforces several quality checks:

    Backend linting, formatting, database migrations, and tests

    Frontend linting and build verification

    Docker image build sanity checks

A passing CI run indicates the code is safe to merge.
MVP Scope

The current MVP focuses on foundational capabilities:

    CSV-based ingestion for sales and labor data

    Canonical data modeling

    Daily and weekly metric computation

    Insight and recommendation framework

    Local-first infrastructure and tooling

The following items are intentionally out of scope for the MVP:

    Production deployment

    Real-time third-party integrations

    Advanced authentication and authorization

    Multi-location analytics

Design Principles

    Local-first, cloud-shaped development

    Canonical data and computed metrics over ad-hoc queries

    Explicit configuration and boundaries

    Strong foundations before feature expansion

Disclaimer

This project is under active development. APIs, schemas, and behavior may change as the MVP evolves.
