from abc import ABC, abstractmethod
from datetime import datetime

from src.schemas.field import (
    FieldRequestSchema,
    FieldResponseSchema,
    FieldDatabaseSchema,
)
from src.schemas.result import (
    ResultSchema,
)
from src.models.fields import FieldEntity
from src.models.results import ResultEntity
from sqlalchemy import insert, select
from src.database.setup import async_session_maker


class AbstractRepository(ABC):

    @abstractmethod
    async def set_field(parameters: FieldDatabaseSchema):
        raise NotImplementedError

    @abstractmethod
    async def get_result(limit: int):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    field: FieldEntity = None
    result: ResultEntity = None

    async def set_field(
        self,
        parameters: FieldDatabaseSchema,
    ) -> FieldResponseSchema:
        async with async_session_maker() as session:
            stmt = (
                insert(self.field)
                .values(field=str(parameters.field), created=datetime.now())
                .returning(self.field.id)
            )
            res = await session.execute(stmt)

            id_field = res.fetchone()[0]

            stmt = insert(self.result).values(
                id_field=id_field, username=parameters.first_user, score=0
            )
            res = await session.execute(stmt)

            stmt = insert(self.result).values(
                id_field=id_field, username=parameters.second_user, score=0
            )
            res = await session.execute(stmt)

            await session.commit()
            # print("--------------------", res.fetchone()[0])

            return FieldResponseSchema(
                first_user=parameters.first_user,
                second_user=parameters.second_user,
                field=parameters.field,
                id=id_field,
            )

    async def get_result(
        self,
        limit: int,
    ) -> list:
        async with async_session_maker() as session:
            pass
            stmt = (
                select(
                    self.result.id_field,
                    self.result.username,
                    self.result.score,
                )
                .select_from(self.result)
                .join(self.field, self.field.id == self.result.id_field)
                .where(self.field.is_complete == 1)
                .limit(limit)
            )
            res = await session.execute(stmt)

            return res.all()
