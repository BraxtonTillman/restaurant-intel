# Restaurant Intel — Frontend

Next.js (App Router) UI for the Restaurant Intelligence Platform. Displays metrics and insights backed by the FastAPI backend.

## Run locally

**With Docker (recommended):** From the repo root, follow the main [README](../README.md). Start all services with:

```bash
make dev
```

The frontend is then available at <http://localhost:3000>.

**Without Docker:** From this directory, with Node.js and pnpm installed:

```bash
pnpm install
pnpm dev
```

Set `NEXT_PUBLIC_API_URL` (e.g. `http://localhost:8000`) so the app can reach the backend. See root `.env.example` for all env vars.

## Tech

- Next.js 16 (App Router)
- TypeScript
- Tailwind CSS
- pnpm

## Commands

From repo root:

- `make frontend-lint` — lint  
- `make frontend-build` — production build  

From this directory:

- `pnpm dev` — dev server  
- `pnpm build` — build  
- `pnpm start` — run production build  
- `pnpm lint` — ESLint  

For full setup, env vars, and architecture, see the [root README](../README.md).
