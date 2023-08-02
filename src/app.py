import logging
import os

from fastapi import FastAPI
from src import settings
from src.api.router import router

logger = logging.getLogger(__name__)

# Initialize FastAPI
app = FastAPI(
    title=settings.TITLE,
    description=settings.DESCRIPTION,
    debug=settings.DEBUG,
    docs_url='/docs' if settings.DEBUG else None,
    redoc_url='/redoc' if settings.DEBUG else None,
)


@app.on_event('startup')
async def startup():
    """
    Keep this order because services depends on repos.
    """
    logger.info("startup: Starting the app")

app.include_router(router, prefix='/v1')

BASE_DIR = os.path.dirname(__file__)
