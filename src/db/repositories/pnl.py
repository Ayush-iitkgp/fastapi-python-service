from src.db.tables.pnl import Pnl
from src.db.repositories.base import BaseRepository
from src.models.pnl import PnlSchema, InPnlSchema
from typing import Type


class PnlRepository(BaseRepository):

    @property
    def _table(self) -> Type[Pnl]:
        return Pnl

    @property
    def _db_schema(self) -> Type[PnlSchema]:
        return PnlSchema

    @property
    def _in_create_schema(self) -> Type[InPnlSchema]:
        return InPnlSchema