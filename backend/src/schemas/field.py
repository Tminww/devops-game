from datetime import date, datetime
from pydantic import BaseModel, validator
from typing import Optional, List


class FieldRequestShema(BaseModel):
    first_user: str
    second_user: str


class FieldDatabaseShema(FieldRequestShema):
    field: str


class FieldResponseShema(FieldRequestShema):
    id: int
    field: List[list]
