from sqlalchemy import Column, String, Integer, ForeignKey, Date, Numeric
from src.db.base_class import Base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Currency(Base):
    __tablename__ = "currency"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    currency_code = Column(String(3), nullable=False)


class Pnl(Base):
    __tablename__ = "pnl"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    currency_id = Column(UUID(as_uuid=True), ForeignKey('currency.id'), nullable=False)
    data_key = Column(String(50), nullable=False)
    data_value = Column(Numeric, nullable=False)
    report_date = Column(Date, nullable=False)

    # Define the relationship to the Currency table
    currency = relationship('Currency', backref='pnls')

