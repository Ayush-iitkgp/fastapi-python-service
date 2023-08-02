import logging

from src.db.tables.pnl import Pnl
from src.db.repositories.base import BaseRepository
from src.models.pnl import PnlSchema, InPnlSchema
from typing import Type, List
from uuid import UUID
from sqlalchemy import delete, select

logger = logging.getLogger(__name__)


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

    async def get_pnl_by_currency_id(self, currency_id: UUID) -> List[PnlSchema]:
        stmt = select(self._table).where(self._table.currency_id == currency_id)
        results = await self._db_session.execute(stmt)
        entries = results.scalars().all()
        if not entries:
            return []
        return [self._db_schema.from_orm(entry) for entry in entries]
    
    async def delete_pnl_by_currency_id(self, currency_id: UUID) -> None:
        stmt = delete(self._table).where(self._table.currency_id == currency_id)
        results = await self._db_session.execute(stmt)
        if results.rowcount == 0:
            logger.info(f"{self._table.__name__}:{currency_id}> does not exist")