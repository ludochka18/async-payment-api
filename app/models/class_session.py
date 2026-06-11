from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class ClassSession(Base):
    __tablename__ = "class_sessions"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    trainer_id: Mapped[int] = mapped_column(
        ForeignKey("trainers.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    location_id: Mapped[int] = mapped_column(
        ForeignKey("studio_locations.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    start_time: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    end_time: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    capacity: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    trainer = relationship(
        "Trainer",
        back_populates="class_sessions",
    )

    location = relationship(
        "StudioLocation",
        back_populates="class_sessions",
    )

    bookings = relationship(
        "Booking",
        back_populates="class_session",
        cascade="all, delete-orphan",
    )
