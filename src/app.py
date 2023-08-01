import logging
import os

from fastapi import FastAPI
from src import settings
from src.api.router import router
# from src.utils import db
# from src.utils.init_app import init_controllers
# from src.utils.init_app import init_repositories
# from src.utils.init_app import init_services
# from src.utils.init_app import init_use_cases


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
    logger.info("Starting the app")
    # await db.boot(app)
    # await init_repositories(app)
    # await init_services(app)
    # await init_use_cases(app)
    # await init_controllers(app)
    # pass

app.include_router(router, prefix='/v1')

BASE_DIR = os.path.dirname(__file__)
