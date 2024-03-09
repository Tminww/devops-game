from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import (
    String,
)

from src.models.base import Base


class UserEntity(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(16))
