import uuid
from typing import Callable

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src import settings
from src.models.pnl import PnlSchema
from src.models.currency import CurrencySchema

pytestmark = pytest.mark.asyncio


async def test_delete_user_benefits_no_auth(
    async_client_for_customer: AsyncClient,
    db_session: AsyncSession,
) -> None:
    response = await async_client_for_customer.delete(f"/pnl/{uuid.uuid4()}/")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


async def test_delete_unlocks_benefits(
    async_client_auth_admin: AsyncClient,
    db_session: AsyncSession,
    currency_factory: Callable[..., CurrencySchema],
    pnl_factory: Callable[..., PnlSchema]

) -> None:
    currency = currency_factory()
    pnl = pnl_factory()
    db_session.add(currency)
    db_session.add(pnl)
    await db_session.commit()

    response = await async_client_auth_admin.delete(
        f"/pnl/{currency.id}/",
        auth=(settings.ADMIN_AUTH_USERNAME, settings.ADMIN_AUTH_PASSWORD),
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT