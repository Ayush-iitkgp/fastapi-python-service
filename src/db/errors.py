from src.exceptions.pnl import BaseError


class BaseDBError(BaseError):
    pass


class DoesNotExist(BaseDBError):
    """Raised when record was not found in database."""