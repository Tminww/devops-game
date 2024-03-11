from abc import ABC, abstractmethod
from datetime import datetime

from src.schemas.field import (
    FieldRequestShema,
    FieldResponseShema,
)
from src.models.fields import FieldEntity
from src.models.results import FieldEntity
from sqlalchemy import (
    insert,
    select,
    func,
)
from src.database.setup import async_session_maker


class AbstractRepository(ABC):
    @abstractmethod
    async def set_field(parameters: FieldRequestShema):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    field: FieldEntity = None

    async def set_field(
        self,
        parameters: FieldRequestShema,
    ):
        async with async_session_maker() as session:
            stmt = insert(self.field).values(parameters).returning("id")
            res = await session.execute(stmt)

            return res
