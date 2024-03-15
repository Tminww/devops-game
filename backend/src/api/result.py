from typing import Annotated
from src.utils import utils
from fastapi import APIRouter

router = APIRouter(
    prefix="/result",
    tags=["Result board"],
)


@router.get("")
async def get_results():
    return {"message": "success"}


@router.post("")
async def set_field(
    field_service: Annotated[FieldService, Depends(field_service)],
    parameters: FieldRequestSchema,
) -> FieldResponseSchema:
    response = await field_service.set_field(parameters=parameters)
    return response
