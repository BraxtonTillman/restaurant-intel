import os
import sys
from logging.config import fileConfig

from alembic import context
from app.db.base import Base
from dotenv import load_dotenv
from sqlalchemy import engine_from_config, pool

load_dotenv()  # loads backend/.env by default if present


# Add backend/app to path so we can import modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# Import your Base and models
# Import all models here for autogenerate to work
# from app.models import *  # Uncomment when you have models

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

print("DATABASE_URL:", os.getenv("DATABASE_URL")) # Debug print to verify env variable
# CRITICAL FIX: Override database URL from environment
database_url = os.getenv("DATABASE_URL")
if database_url:
    config.set_main_option("sqlalchemy.url", database_url)

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
