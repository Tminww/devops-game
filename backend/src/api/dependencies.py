from src.repositories.field import FieldRepository
from src.services.field import FieldService

from src.repositories.result import ResultRepository
from src.services.result import ResultService


def field_service():
    return FieldService(FieldRepository)


def result_service():
    return ResultService(ResultRepository)
