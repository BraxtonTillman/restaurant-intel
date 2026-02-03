"""Add sales_orders table

Revision ID: c54fe3241012
Revises: 04723d25ab9f
Create Date: 2026-02-03 13:04:57.728100

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "c54fe3241012"
down_revision: str | Sequence[str] | None = "04723d25ab9f"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade():
    op.create_table(
        "sales_orders",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column(
            "ingestion_run_id",
            sa.Integer(),
            sa.ForeignKey("ingestion_runs.id"),
            nullable=False,
        ),
        sa.Column("order_id", sa.String(length=100), nullable=False),
        sa.Column(
            "occurred_at", sa.DateTime(), server_default=sa.func.now(), nullable=False
        ),
        sa.Column("total", sa.Float()),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.func.now(), nullable=False
        ),
    )


def downgrade():
    op.drop_table("sales_orders")
