import pytest
from app.services.price_service import PriceService


@pytest.mark.asyncio
async def test_save_and_get_latest_price(db_session):
    service = PriceService(db_session)

    await service.save_price("BTC_USD", 100.0)
    await service.save_price("BTC_USD", 200.0)

    latest = await service.get_latest_price("BTC_USD")

    assert latest is not None
    assert latest.price == 200.0
    assert latest.ticker == "BTC_USD"
