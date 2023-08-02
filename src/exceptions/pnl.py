class BaseError(Exception):
    pass


class PnlError(BaseError):
    pass


class CurrencyNotFoundError(PnlError):
    pass


class PnlNotUpdatedError(PnlError):
    pass
