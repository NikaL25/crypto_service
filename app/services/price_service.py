from datetime import datetime
from typing import List, Optional

from app.repositories.price_repository import PriceRepository
from app.models.price import Price


class PriceService:

    def __init__(self, repository: PriceRepository):
        self.repository = repository

    async def save_price(
        self,
        ticker: str,
        price: float,
        timestamp: datetime
    ) -> Price:

        ticker = ticker.upper()

        return await self.repository.create(
            ticker=ticker,
            price=price,
            timestamp=timestamp,
        )

    async def get_latest_price(
        self,
        ticker: str
    ) -> Optional[Price]:

        return await self.repository.get_latest(
            ticker.upper()
        )

    async def get_all_prices(
        self,
        ticker: str
    ) -> List[Price]:

        return await self.repository.get_all(
            ticker.upper()
        )

    async def get_prices_by_date(
        self,
        ticker: str,
        date_from: int,
        date_to: int,
    ) -> List[Price]:

        start = datetime.utcfromtimestamp(date_from)
        end = datetime.utcfromtimestamp(date_to)

        return await self.repository.get_range(
            ticker.upper(),
            start,
            end
        )
