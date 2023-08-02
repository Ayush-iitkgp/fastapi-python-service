from src.db.tables.pnl import Currency
from src.db.repositories.base import BaseRepository
from src.models.currency import CurrencySchema, InCurrencySchema
from typing import Type
import logging

logger = logging.getLogger(__name__)


class CurrencyRepository(BaseRepository):
    @property
    def _table(self) -> Type[Currency]:
        return Currency

    @property
    def _db_schema(self) -> Type[CurrencySchema]:
        return CurrencySchema

    @property
    def _in_create_schema(self) -> Type[InCurrencySchema]:
        return InCurrencySchema
