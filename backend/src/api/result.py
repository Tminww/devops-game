from typing import Annotated
from fastapi import APIRouter, Depends

from src.api.dependencies import result_service
from src.services.result import ResultService
from src.utils import utils

from src.schemas.result import (
    ResultSchema,
)

router = APIRouter(
    prefix="/result",
    tags=["Result board"],
)


@router.get("")
async def get_results(
    result_service: Annotated[ResultService, Depends(result_service)],
    limit: int = 10,
) -> ResultSchema:
    response = await result_service.set_field(limit)
    return response
