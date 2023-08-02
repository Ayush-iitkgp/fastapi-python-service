import logging
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.repositories.pnl import PnlRepository
from src.db.repositories.currency import CurrencyRepository
from src.models.schema.out_pnl import OutDataPnlSchema, OutPnlSchema
from src.db.errors import DoesNotExist
from src.exceptions.pnl import CurrencyNotDeletedError, CurrencyNotFoundError
logger = logging.getLogger(__name__)


class PnlService:

    @classmethod
    async def get_pnl_by_currency_id(
            cls,
            db: AsyncSession,
            currency_id: UUID,
    ) -> OutDataPnlSchema:
        currency_repository = CurrencyRepository(db_session=db)
        pnl_repository = PnlRepository(db_session=db)
        try:
            currency = await currency_repository.get_by_id(entry_id=currency_id)
            pnl = await pnl_repository.get_pnl_by_currency_id(currency_id=currency.id)
        except DoesNotExist:
            raise CurrencyNotFoundError
        return OutDataPnlSchema(
            data=OutPnlSchema(id=currency.id, currency_code=currency.currency_code, pnl=pnl))

    @classmethod
    async def delete_pnl_by_currency_id(
            cls,
            db: AsyncSession,
            currency_id: UUID,
    ) -> None:
        pnl_repository = PnlRepository(db_session=db)
        currency_repository = CurrencyRepository(db_session=db)
        try:
            currency = await currency_repository.get_by_id(entry_id=currency_id)
        except DoesNotExist:
            raise CurrencyNotFoundError

        try:
            await pnl_repository.delete_pnl_by_currency_id(currency_id=currency.id)
            await currency_repository.delete_by_id(entry_id=currency.id)
            await db.commit()
        except Exception:
            await db.rollback()
            raise CurrencyNotDeletedError

