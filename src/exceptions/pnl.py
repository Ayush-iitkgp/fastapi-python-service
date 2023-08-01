class PnlError(Exception):
    pass


class CurrencyNotFoundError(PnlError):
    pass


class PnlNotUpdatedError(PnlError):
    pass
