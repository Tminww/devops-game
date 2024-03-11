from src.schemas.field import (
    FieldRequestSchema,
    FieldResponseSchema,
    FieldDatabaseSchema,
)
from src.utils.repository import AbstractRepository
from src.utils import utils


class FieldService:
    def __init__(self, field_repo: AbstractRepository):
        self.field_repo: AbstractRepository = field_repo()

    async def set_field(self, parameters: FieldRequestSchema) -> FieldResponseSchema:

        field = utils.GameField(row=21, column=47).get_field()
        utils.GameField.print_field(field)

        response = await self.field_repo.set_field(
            FieldDatabaseSchema(
                first_user=parameters.first_user,
                second_user=parameters.second_user,
                field=field,
            )
        )
        return response
