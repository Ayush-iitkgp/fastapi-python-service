import logging
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from src import settings
logger = logging.getLogger(__name__)


async def boot(app):
    setup_postgresdb(app)
    # await create_tables()
    logger.info(
        'boot: Database connection succeeded')


def setup_postgresdb(app: FastAPI) -> None:
    """
    Helper function to set up Postgres connection
    """
    client = create_db_client()
    app.postgres = client
    app.db = client


def create_db_client():
    engine = create_async_engine(
        settings.DATABASE_URL,
        pool_size=settings.DATABASE_POOL_SIZE,
        pool_pre_ping=True,
        echo=True,
    )
    return sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def create_tables():
    pass
