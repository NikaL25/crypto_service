import pytest
from datetime import datetime

from app.repositories.price_repository import PriceRepository
from app.services.price_service import PriceService


@pytest.mark.asyncio
async def test_save_and_get_all(db_session):

    repo = PriceRepository(db_session)

    service = PriceService(repo)

    await service.save_price(
        "BTC_USD",
        100,
        datetime.utcnow()
    )

    prices = await service.get_all_prices("BTC_USD")

    assert len(prices) == 1
