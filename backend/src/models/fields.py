from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, DateTime
from typing import List
from src.models.base import Base


class FieldEntity(Base):
    __tablename__ = "fields"

    id: Mapped[int] = mapped_column(primary_key=True)
    field: Mapped[str] = mapped_column(Text)
    created: Mapped[datetime] = mapped_column(DateTime)
    is_complete: Mapped[bool] = mapped_column(default=0)
