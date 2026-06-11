from datetime import datetime
from enum import Enum

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class UserRole(str, Enum):
    CLIENT = "client"
    ADMIN = "admin"
    TRAINER = "trainer"


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False,
    )

    full_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    hashed_password: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    role: Mapped[str] = mapped_column(
        String(50),
        default=UserRole.CLIENT.value,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    subscriptions = relationship(
        "Subscription",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    payments = relationship(
        "Payment",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    bookings = relationship(
        "Booking",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    trainer_profile = relationship(
        "Trainer",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan",
    )
