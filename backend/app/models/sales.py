'''
Docstring for backend.app.models.sales
'''

from datetime import datetime
from enum import Enum

from app.db.base import Base
from sqlalchemy import DateTime
from sqlalchemy import Enum as SQLEnum
from sqlalchemy import Float, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship


# This class checks the status of the ingestion run.
# Will return uploaded, failed, or processed
class IngestionStatus(str, Enum):
    UPLOADED = "uploaded"
    PROCESSED = "processed"
    FAILED = "failed"

# This class tracks each CSV file ingestion attempt
# One ingestion_run can have many sales_orders (one to many)
class IngestionRun(Base):
    __tablename__ = "ingestion_runs"

    id: Mapped[int] = mapped_column(primary_key=True)
    source: Mapped[str] = mapped_column(String(255))
    status: Mapped[IngestionStatus] = mapped_column(
        SQLEnum(IngestionStatus, name="ingestion_status"),
        default=IngestionStatus.UPLOADED,
        nullable=False,
    )
    file_path: Mapped[str] = mapped_column(String(500))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # Relationships to sales orders
    sales_orders: Mapped[list["SalesOrder"]] = relationship(
        back_populates="ingestion_run",
        cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<IngestionRun(id={self.id}, source={self.source}, status{self.status})>"


class SalesOrder(Base):
    """
    Individual sales order records from CSV files.

    Each order is linked to an ingestion_run
    """
    __tablename__ = "sales_orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    ingestion_run_id: Mapped[int] = mapped_column(
        ForeignKey("ingestion_runs.id", ondelete="CASCADE")
    )
    order_id: Mapped[str] = mapped_column(String(255), index=True)
    occurred_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    total: Mapped[float] = mapped_column(Float)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    # Relationship back to ingestion run
    ingestion_run: Mapped["IngestionRun"] = relationship(back_populates="sales_orders")

    def __repr__(self):
        return f"<SalesOrder(id={self.id}, order_id={self.order_id}, total={self.total})>"


