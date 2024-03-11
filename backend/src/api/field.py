from typing import Annotated
from fastapi import Depends, APIRouter
from src.api.dependencies import field_service
from src.services.field import FieldService
from src.utils import utils

from src.schemas.field import (
    FieldRequestShema,
    FieldResponseShema,
)


router = APIRouter(
    prefix="/field",
    tags=["Game field"],
)


# @router.get("", response_model=None)
# async def get_results(field: utils.GameField):
#     field = utils.Field(row=21, column=47)
#     return {"message": "success", "field": field.get_field()}


@router.post("")
async def get_results(
    field_service: Annotated[FieldService, Depends(field_service)],
    parameters: FieldRequestShema,
):
    response = await field_service.set_field(parameters)
    return {"message": "success", "response": response}
