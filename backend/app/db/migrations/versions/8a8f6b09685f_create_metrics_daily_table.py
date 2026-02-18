"""Create metrics_daily table

Revision ID: 8a8f6b09685f
Revises: c54fe3241012
Create Date: 2026-02-18 12:31:04.908690

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '8a8f6b09685f'
down_revision: Union[str, Sequence[str], None] = 'c54fe3241012'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "metrics_daily",
        sa.Column("date", sa.Date(), primary_key=True),
        sa.Column("sales_total", sa.Float()),
        sa.Column("order_count", sa.Integer()),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("metrics_daily")
