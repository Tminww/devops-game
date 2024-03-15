from src.schemas.result import (
    ResultSchema,
    UserSchema,
    ResultResponseSchema,
)
from src.utils.repository import AbstractRepository
from src.utils import utils


class ResultService:
    def __init__(self, result_repo: AbstractRepository):
        self.result_repo: AbstractRepository = result_repo()

    async def get_result(self, limit: int) -> ResultResponseSchema:

        response = await self.result_repo.get_result(limit)

        return ResultResponseSchema(response=response, count=len(response))
