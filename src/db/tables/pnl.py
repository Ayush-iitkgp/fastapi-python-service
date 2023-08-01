from sqlalchemy import Column, String


class Currency:
    __tablename__ = "currency"

    currency_id = Column(String, unique=True, nullable=False)
    currency_code = Column(String, nullable=False)


class Pnl:
    __tablename__ = "pnl"
    currency_id = Column(String, unique=True, nullable=False)
    currency_code = Column(String, nullable=False)

