from src.repositories.field import FieldRepository

from src.services.field import FieldService


def field_service():
    return FieldService(FieldRepository)
