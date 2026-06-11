from datetime import date, datetime
from enum import Enum

from sqlalchemy import Date, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class SubscriptionStatus(str, Enum):
    ACTIVE = "active"
    EXPIRED = "expired"
    FROZEN = "frozen"


class Subscription(Base):
    __tablename__ = "subscriptions"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    total_classes: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    remaining_classes: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    valid_until: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default=SubscriptionStatus.ACTIVE.value,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    user = relationship(
        "User",
        back_populates="subscriptions",
    )

    payments = relationship(
        "Payment",
        back_populates="subscription",
    )
