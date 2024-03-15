from typing import Annotated
from fastapi import APIRouter, Depends

from src.api.dependencies import result_service
from src.services.result import ResultService
from src.utils import utils

from src.schemas.result import (
    ResultSchema,
    ResultResponseSchema,
)

router = APIRouter(
    prefix="/result",
    tags=["Result board"],
)


@router.get("")
async def get_results(
    result_service: Annotated[ResultService, Depends(result_service)],
    limit: int = 10,
) -> ResultResponseSchema:
    response = await result_service.get_result(limit)
    return response
