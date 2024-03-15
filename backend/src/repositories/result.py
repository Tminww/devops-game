from src.models.fields import FieldEntity
from src.models.results import ResultEntity


from src.utils.repository import SQLAlchemyRepository


class ResultRepository(SQLAlchemyRepository):
    field = FieldEntity
    result = ResultEntity
