from datetime import date, datetime
from pydantic import BaseModel, validator
from typing import Optional, List


class ResultSchema(BaseModel):
    first_user: str
    second_user: str


class FieldDatabaseSchema(FieldRequestSchema):
    field: List[list]


class FieldResponseSchema(FieldRequestSchema):
    id: int
    field: List[list]
