from typing import Annotated
from src.utils import utils
from fastapi import APIRouter

router = APIRouter(
    prefix="/board",
    tags=["Result board"],
)


@router.get("")
async def get_results():
    return {"message": "success"}
