# Restaurant Intel — Frontend (CRUD UI)

This directory contains the Next.js frontend for a simple restaurant‑themed CRUD app.  
It is a small learning UI that talks to the FastAPI backend and lets you list, create, edit, and delete records.

---

## What this frontend does

- Renders basic pages and forms for CRUD operations.
- Calls the backend API to load and save data.
- Uses Tailwind for quick styling and layout.

It is intentionally minimal and focused on wiring the browser to the API and database.

---

## Run locally

**With Docker (recommended):** From the repo root, follow the main [README](../README.md). Start all services with:

```bash
make dev
```

The frontend will be available at <http://localhost:3000>.

**Without Docker:** From this directory, with Node.js and pnpm installed:

```bash
pnpm install
pnpm dev
```

Set `NEXT_PUBLIC_API_URL` (for example `http://localhost:8000`) so the app can reach the backend.  
See the root `.env.example` for the relevant variables.

---

## Tech

- Next.js (App Router)
- TypeScript
- Tailwind CSS
- pnpm

---

## Useful commands

From the repo root:

- `make frontend-lint` — lint the frontend  
- `make frontend-build` — production build  

From this directory:

- `pnpm dev` — dev server  
- `pnpm build` — build  
- `pnpm start` — run the production build  
- `pnpm lint` — ESLint  

For the bigger picture of how this fits into the app, see the [root README](../README.md).
