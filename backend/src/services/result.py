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

    async def get_result(self, limit: int) -> ResultSchema:

        response = await self.result_repo.get_result(limit)

        game_result: dict = {}

        for item in response:
            key = str(item[0])
            if key not in game_result:
                game_result[key] = []
            game_result[key].append({"username": item[1], "score": item[2]})

        print("------------", game_result)

        response = []
        for value in game_result.values():
            response.append(value)

        # for id_feld, username, score in response:

        #     game_result[id_feld] =
        #     print(id_feld, username, score)
        #     print(game_result)

        return response
