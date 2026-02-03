FROM node:20-slim

WORKDIR /app

# Enable corepack for pnpm
RUN corepack enable

# Copy package files
COPY package.json pnpm-lock.yaml ./

# Install dependencies
RUN pnpm install --frozen-lockfile

# Copy rest of app
COPY . .

EXPOSE 3000

# Use pnpm consistently
CMD ["pnpm", "dev", "--hostname", "0.0.0.0", "--port", "3000"]
