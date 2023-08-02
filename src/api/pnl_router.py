from fastapi import APIRouter
from fastapi import Request
from starlette import status
import uuid
from src.models.schema.out_pnl import OutDataPnlSchema
from src.db.session import async_session
from src.services.pnl_service import pnl_service
router = APIRouter()

@router.get(
    "/{currency_id}/", status_code=status.HTTP_200_OK, response_model=OutDataPnlSchema
)
async def get_pnl_for_currency(
    currency_id: uuid.UUID,
) -> OutDataPnlSchema:
    async with async_session() as db:
        benefits_page = await pnl_service.get_pnl_by_currency_id(
            db, currency_id
        )
    return benefits_page


@router.delete(
    "/{currency_id}/", status_code=status.HTTP_204_NO_CONTENT
)
async def get_pnl_for_currency(
    currency_id: uuid.UUID,
) -> None:
    async with async_session() as db:
        benefits_page = await pnl_service.delete_pnl_by_currency_id(
            db, currency_id
        )
        await db.commit()
