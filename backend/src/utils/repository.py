from abc import ABC, abstractmethod
from datetime import datetime
import time

from src.schemas.field import (
    FieldRequestSchema,
    FieldResponseSchema,
    FieldDatabaseSchema,
)
from src.schemas.result import (
    ResultSchema,
    UserSchema,
)
from src.models.fields import FieldEntity
from src.models.results import ResultEntity
from sqlalchemy import insert, select, desc
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
                .values(field=str(parameters.field), created=datetime.now(), is_complete=bool(1))
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
            # time.sleep(2)
            stmt = (
                select(self.field.id, self.field.created)
                .where(self.field.is_complete == 1)
                .limit(limit)
                .order_by(desc(self.field.created))
            )
            res = await session.execute(stmt)

            complete_games = res.all()
            print("-----------------", complete_games)

            response = []
            for id_field, created in complete_games:

                stmt = select(
                    self.result.username,
                    self.result.score,
                ).where(self.result.id_field == id_field)

                res = await session.execute(stmt)
                game_result = res.all()

                print("--------------", game_result, game_result[0], game_result[1])

                response.append(
                    ResultSchema(
                        first_user=UserSchema(
                            username=game_result[0][0],
                            score=game_result[0][1],
                        ),
                        second_user=UserSchema(
                            username=game_result[1][0],
                            score=game_result[1][1],
                        ),
                        created=created,
                    )
                )

            return response
