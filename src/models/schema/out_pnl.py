from datetime import datetime
from math import ceil
from typing import Optional, List
from uuid import UUID

from src.models.basemodel import BaseSchema
from src.models.pnl import PnlSchema


class OutPnlSchema(BaseSchema):
    id: UUID
    currency_code: str
    pnl: List[PnlSchema]


class OutDataPnlSchema(BaseSchema):
    data: OutPnlSchema
