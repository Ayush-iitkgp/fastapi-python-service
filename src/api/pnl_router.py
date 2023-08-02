from fastapi import APIRouter
from starlette import status
import uuid
from src.models.schema.out_pnl import OutDataPnlSchema
from src.db.session import async_session
from src.services.pnl_service import PnlService
router = APIRouter()


@router.get(
    "/{currencyId}/", status_code=status.HTTP_200_OK, response_model=OutDataPnlSchema
)
async def get_pnl_for_currency(
    currencyId: uuid.UUID,
) -> OutDataPnlSchema:
    async with async_session() as db:
        return await PnlService.get_pnl_by_currency_id(db, currencyId)


@router.delete(
    "/{currencyId}/", status_code=status.HTTP_204_NO_CONTENT
)
async def get_pnl_for_currency(
    currencyId: uuid.UUID,
) -> None:
    async with async_session() as db:
        await PnlService.delete_pnl_by_currency_id(db, currencyId)
