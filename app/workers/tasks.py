import asyncio
from datetime import datetime

from celery import shared_task

from app.clients.deribit_client import DeribitClient
from app.db.session import AsyncSessionLocal
from app.repositories.price_repository import PriceRepository
from app.services.price_service import PriceService


TICKERS = [
    "btc_usd",
    "eth_usd",
]


@shared_task(
    autoretry_for=(Exception,),
    retry_backoff=10,
    retry_kwargs={"max_retries": 3},
)
def fetch_crypto_prices():

    asyncio.run(run())


async def run():

    client = DeribitClient()

    async with AsyncSessionLocal() as session:

        repo = PriceRepository(session)
        service = PriceService(repo)

        for ticker in TICKERS:

            price = await client.get_index_price(ticker)

            await service.save_price(
                ticker=ticker,
                price=price,
                timestamp=datetime.utcnow(),
            )

        await session.commit()
