
import asyncio
import logging
from datetime import datetime
from decimal import Decimal
from typing import List, Optional, Tuple, Union
from uuid import UUID

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.repositories.pnl import PnlRepository
from src.db.repositories.currency import CurrencyRepository
from src.models.schema.out_pnl import OutPnlSchema
from src.models.pnl import InPnlSchema
from src.models.currency import InCurrencySchema


class PnlService:

    async def get_pnl_by_currency_id(
        self,
            db: AsyncSession,
        currency_id: UUID,
    ) -> None:
        pnl_repository = PnlRepository(db_session=db)
        currency_repository = CurrencyRepository(db_session=db)
        await pnl_repository.get_by_id(currency_id)

    async def delete_pnl_by_currency_id(
        self,
            db: AsyncSession,
        currency_id: UUID,
    ) -> None:
        pnl_repository = PnlRepository(db_session=db)
        currency_repository = CurrencyRepository(db_session=db)
        await pnl_repository.delete_by_id(currency_id)


pnl_service = PnlService()
