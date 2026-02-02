FROM node:20-slim

WORKDIR /app

# Copy only package files first for caching
COPY package.json package-lock.json* pnpm-lock.yaml* yarn.lock* ./

# Install deps (choose the right command automatically-ish)
# If you know which one you use, delete the other branches.
RUN if [ -f package-lock.json ]; then npm ci; \
  elif [ -f pnpm-lock.yaml ]; then corepack enable && pnpm install --frozen-lockfile; \
  elif [ -f yarn.lock ]; then corepack enable && yarn install --frozen-lockfile; \
  else npm install; fi

# Copy the rest of the app
COPY . .

EXPOSE 3000

CMD ["npm", "run", "dev", "--", "--hostname", "0.0.0.0", "--port", "3000"]
