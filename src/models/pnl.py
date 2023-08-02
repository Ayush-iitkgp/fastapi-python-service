from datetime import date
from src.models.basemodel import BaseSchema
from uuid import UUID


class PnlSchemaBase(BaseSchema):
    currency_id: UUID
    data_key: str
    data_value: float
    report_date: date


class PnlSchema(PnlSchemaBase):
    id: UUID


class InPnlSchema(PnlSchemaBase):
    ...