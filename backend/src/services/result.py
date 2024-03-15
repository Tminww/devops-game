from src.schemas.result import (
    ResultSchema,
)
from src.utils.repository import AbstractRepository
from src.utils import utils


class ResultService:
    def __init__(self, result_repo: AbstractRepository):
        self.result_repo: AbstractRepository = result_repo()

    async def get_result(self, limit: int) -> ResultSchema:

        response = await self.field_repo.set_field(
            FieldDatabaseSchema(
                first_user=parameters.first_user,
                second_user=parameters.second_user,
                field=field,
            )
        )
        return response
