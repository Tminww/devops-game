from datetime import date, datetime
from pydantic import BaseModel, validator
from typing import Optional, List


class UserSchema(BaseModel):
    username: str
    score: int


class ResultSchema(BaseModel):
    first_user: UserSchema
    second_user: UserSchema
    created: datetime


class ResultResponseSchema(BaseModel):
    response: List[ResultSchema]
