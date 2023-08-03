from typing import AsyncGenerator

import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.base_class import Base
from src.db.session import async_session, engine


@pytest.fixture
def app() -> FastAPI:
    from src.app import app
    return app


@pytest.fixture
async def async_client(app: FastAPI) -> AsyncGenerator:
    async with AsyncClient(app=app, base_url="http://localhost:3000") as ac:
        yield ac


@pytest.fixture()
async def db_session() -> AsyncSession:
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)
    async with async_session() as session:
        yield session
        await session.flush()
        await session.rollback()
