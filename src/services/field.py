from src.schemas.field import (
    FieldRequestShema,
    FieldResponseShema,
    FieldDatabaseShema,
)
from src.utils.repository import AbstractRepository
from src.utils import utils


class FieldService:
    def __init__(self, field_repo: AbstractRepository):
        self.field_repo: AbstractRepository = field_repo()

    async def set_field(self, parameters: FieldRequestShema) -> FieldResponseShema:

        field = utils.GameField(row=21, column=47).get_field()

        return FieldResponseShema(
            first_user=parameters.first_user,
            second_user=parameters.second_user,
            id=0,
            field=field,
        )
