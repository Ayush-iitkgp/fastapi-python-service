from datetime import datetime
from math import ceil
from typing import Optional, List
from uuid import UUID

from src.models.basemodel import BaseSchema
from src.models.pnl import PnlSchema


class OutPnlSchema(BaseSchema):
    id: UUID
    currency_code: str
    pnl: List[PnlSchema]

    def get_usable_minutes(
        self,
        valid_after: datetime,
        valid_before: datetime,
    ) -> int:
        if self.minutes_remaining <= 0:
            return 0

        # related to config value _PRICING_ENABLE_PARTIAL_CONTINGENT_DEDUCTION=True on rental service
        # here we calculate how many minutes from ride duration matches benefit validity period
        minutes_remaining = self._calculte_available_minutes(valid_after, valid_before)

        # related to config value _PRICING_ENABLE_FAIR_USAGE=True on rental service
        if self.max_minutes_per_ride:
            return min(self.max_minutes_per_ride, minutes_remaining)

        return minutes_remaining

    def _calculte_available_minutes(self, valid_after: datetime, valid_before: datetime) -> int:
        remaining_minutes = self.minutes_remaining

        valid_from, valid_until = self.valid_from, self.valid_until
        start = max(valid_from, valid_after) if valid_from else valid_after
        end = min(valid_until, valid_before) if valid_until else valid_before

        if start and end:
            valid_minutes = ceil((end - start).total_seconds() / 60)
            remaining_minutes = min(remaining_minutes, valid_minutes)
        return max(0, remaining_minutes)


class OutDataPnlSchema(BaseSchema):
    data: OutPnlSchema
