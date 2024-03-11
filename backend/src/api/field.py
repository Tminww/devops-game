from typing import Annotated
from fastapi import Depends, APIRouter
from src.api.dependencies import field_service
from src.services.field import FieldService
from src.utils import utils

from src.schemas.field import (
    FieldRequestSchema,
    FieldResponseSchema,
)


router = APIRouter(
    prefix="/field",
    tags=["Game field"],
)


@router.post("")
async def set_field(
    field_service: Annotated[FieldService, Depends(field_service)],
    parameters: FieldRequestSchema,
) -> FieldResponseSchema:
    response = await field_service.set_field(parameters=parameters)
    return response
