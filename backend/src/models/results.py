from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Text
from typing import List
from src.models.base import Base


class ResultEntity(Base):
    __tablename__ = "results"

    id: Mapped[int] = mapped_column(primary_key=True)
    id_field: Mapped[int] = mapped_column(ForeignKey("fields.id"))
    username: Mapped[str] = mapped_column(String(16))
    score: Mapped[int]
