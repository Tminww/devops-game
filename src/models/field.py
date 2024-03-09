from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text
from typing import List
from src.models.base import Base


class FieldEntity(Base):
    __tablename__ = "fields"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_user: Mapped[str] = mapped_column(String(16))
    second_user: Mapped[str] = mapped_column(String(16))
    field: Mapped[str] = mapped_column(Text)
