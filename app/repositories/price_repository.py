from datetime import datetime
from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.price import Price


class PriceRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(
        self,
        ticker: str,
        price: float,
        timestamp: datetime
    ) -> Price:

        obj = Price(
            ticker=ticker,
            price=price,
            timestamp=timestamp
        )

        self.session.add(obj)
        await self.session.flush()

        return obj

    async def get_latest(self, ticker: str) -> Optional[Price]:

        stmt = (
            select(Price)
            .where(Price.ticker == ticker)
            .order_by(Price.timestamp.desc())
            .limit(1)
        )

        result = await self.session.execute(stmt)

        return result.scalars().first()

    async def get_all(self, ticker: str) -> List[Price]:

        stmt = (
            select(Price)
            .where(Price.ticker == ticker)
            .order_by(Price.timestamp)
        )

        result = await self.session.execute(stmt)

        return list(result.scalars())

    async def get_range(
        self,
        ticker: str,
        start: datetime,
        end: datetime
    ) -> List[Price]:

        stmt = (
            select(Price)
            .where(
                Price.ticker == ticker,
                Price.timestamp >= start,
                Price.timestamp <= end,
            )
            .order_by(Price.timestamp)
        )

        result = await self.session.execute(stmt)

        return list(result.scalars())