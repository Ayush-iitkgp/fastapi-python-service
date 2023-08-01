import os
import time

import uvicorn

from src import settings

# Setup timezone info
os.environ['TZ'] = settings.TIMEZONE
time.tzset()

if __name__ == '__main__':
    uvicorn.run(app="src.app:app",
                host=settings.HOST,
                port=settings.PORT)
