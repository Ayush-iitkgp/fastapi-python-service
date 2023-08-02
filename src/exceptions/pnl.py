from fastapi import HTTPException
from starlette import status
from typing import Dict, Optional, Any


class BaseError(HTTPException):
    pass


class PnlError(BaseError):
    pass


class CurrencyNotFoundError(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail="Currency not found")


class CurrencyNotDeletedError(PnlError):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Currency record could not be deleted")


class HTTPUnauthorizedError(HTTPException):
    def __init__(
        self,
        detail: str = "HTTP unauthorized error",
        headers: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail=detail, headers=headers)