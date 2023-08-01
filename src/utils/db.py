import logging
from fastapi import FastAPI
# from sqlalchemy import create_engine

# from src import settings

logger = logging.getLogger(__name__)


async def boot(app):
    pass
    # try:
    #     setup_postgresdb(app, settings)
    #     await create_tables()
    #     connection_status = await get_connection_status(app.mongodb)
    #     logger.info(
    #         'Database connection succeeded',
    #         extra={'connection_status': connection_status},
    #     )
    # except OperationFailure as exc:
    #     logger.error(
    #         'Database connection failed',
    #         exc_info=exc,
    #     )
    # except Exception as exc:
    #     logger.critical(
    #         'Unknown error occurred while trying to establish to database connection',
    #         exc_info=exc,
    #     )


async def get_connection_status(db):
    return await db.command({'connectionStatus': 1})


def setup_postgresdb(app: FastAPI, settings) -> None:
    """
    Helper function to setup Postgres connection
    """
    pass

    # client = create_db_client(settings)
    # app.postgres = client
    # app.db = client


def create_db_client(settings):
    # engine = create_engine(settings.DATABASE_URL)

    # client = motor.motor_asyncio.AsyncIOMotorClient(
    #     settings.DATABASE_URL,
    #     minPoolSize=db_settings.mongodb_min_pool_size,
    #     maxPoolSize=db_settings.mongodb_max_pool_size,
    #     tls=settings.DATABASE_TLS_ENABLED,
    #     tlsCAFile=settings.DATABASE_TLS_CA_FILE,
    # )
    pass

    # return client[settings.DATABASE_NAME]


async def create_tables():
    pass
    # from ride.models import Ride
    # await Ride.create_indexes()