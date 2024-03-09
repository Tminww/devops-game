from typing import Annotated

from fastapi import APIRouter

router = APIRouter(
    prefix="/board",
    tags=["Result board"],
)


@router.get("")
async def get_results():
    return {"message": "success"}
