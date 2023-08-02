from src.models.basemodel import BaseSchema
from uuid import UUID


class CurrencySchemaBase(BaseSchema):
    currency_code: str


class CurrencySchema(CurrencySchemaBase):
    id: UUID
    currency_code: str


class InCurrencySchema(CurrencySchemaBase):
    ...

