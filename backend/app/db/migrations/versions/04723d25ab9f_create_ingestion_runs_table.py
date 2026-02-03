"""create ingestion_runs table

Revision ID: 04723d25ab9f
Revises:
Create Date: 2026-02-03 10:22:17.675355

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '04723d25ab9f'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    status_enum = sa.Enum("uploaded", "processed", "failed", name="ingestion_status",)

    status_enum.create(op.get_bind(), checkfirst=True)

    op.create_table(
        'ingestion_runs',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('source', sa.String(length=255), nullable=False),
        sa.Column('status', sa.String(length=50), nullable=False),
        sa.Column('file_path', sa.String(length=1024), nullable=True),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime, server_default=sa.func.now(), nullable=False),
    )


def downgrade():
    op.drop_table('ingestion_runs')
    status_enum = sa.Enum("uploaded", "processed", "failed", name="ingestion_status",)
    status_enum.drop(op.get_bind(), checkfirst=True)

