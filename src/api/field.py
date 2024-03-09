from typing import Annotated

from fastapi import APIRouter

router = APIRouter(
    prefix="/field",
    tags=["Game field"],
)


@router.get("")
async def get_results():

    return {"message": "success"}
