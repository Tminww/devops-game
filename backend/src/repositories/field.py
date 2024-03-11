from src.models.fields import FieldEntity


from src.utils.repository import SQLAlchemyRepository


class FieldRepository(SQLAlchemyRepository):
    field = FieldEntity
