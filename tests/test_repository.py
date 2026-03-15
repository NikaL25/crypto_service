import pytest
from datetime import datetime

from app.repositories.price_repository import PriceRepository


@pytest.mark.asyncio
async def test_create_and_get_latest(db_session):

    repo = PriceRepository(db_session)

    await repo.create("BTC_USD", 100, datetime.utcnow())
    await repo.create("BTC_USD", 200, datetime.utcnow())

    latest = await repo.get_latest("BTC_USD")

    assert latest is not None
    assert latest.price == 200
