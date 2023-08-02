import secrets

from fastapi import Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from src import settings
from src.exceptions.pnl import HTTPUnauthorizedError

security = HTTPBasic()


class BasicAutorization:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def __call__(self, credentials: HTTPBasicCredentials = Depends(security)) -> str:
        given_username, given_password = (
            credentials.username or "",
            credentials.password or "",
        )
        correct_username = secrets.compare_digest(given_username, self.username)
        correct_password = secrets.compare_digest(given_password, self.password)

        if not (correct_username and correct_password):
            raise HTTPUnauthorizedError

        return given_username


basic_auth = BasicAutorization(username=settings.ADMIN_AUTH_USERNAME, password=settings.ADMIN_AUTH_PASSWORD)
