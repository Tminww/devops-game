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
from sqlalchemy import (
    insert,
    select,
    func,
)
from src.database.setup import async_session_maker


class AbstractRepository(ABC):

    @abstractmethod
    async def set_field(parameters: FieldDatabaseSchema):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    field: FieldEntity = None
    result: ResultEntity = None

    async def set_field(
        self,
        parameters: FieldDatabaseSchema,
    ):
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
    ):
        async with async_session_maker() as session:
            pass
            # select(
            #         self.result.name.label("name"),
            #         func.count().label("count"),
            #     )
            #     .select_from(self.document)
            #     .join(self.region, self.document.id_reg == self.region.id)
            #     .join(self.act, self.document.id_act == self.act.id)
            #     .filter(
            # res = await session.execute(stmt)

            # return FieldResponseSchema(
            #     first_user=parameters.first_user,
            #     second_user=parameters.second_user,
            #     field=parameters.field,
            #     id=id_field,
            # )
