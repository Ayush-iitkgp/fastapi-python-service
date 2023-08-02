from datetime import date
from src.models.basemodel import BaseSchema
from uuid import UUID


class PnlSchemaBase(BaseSchema):
    currency_id: UUID
    financial_item: str
    financial_value: float
    report_date: date


class PnlSchema(PnlSchemaBase):
    id: UUID


class InPnlSchema(PnlSchemaBase):
    ...