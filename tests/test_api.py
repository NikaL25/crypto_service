import pytest


@pytest.mark.asyncio
async def test_get_latest_price_endpoint(client):
    await client.get("/prices/all?ticker=BTC_USD")  

    response = await client.get("/prices/latest?ticker=BTC_USD")
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_get_all_prices(client):
    await client.get("/prices/latest?ticker=BTC_USD")

    response = await client.get("/prices/all?ticker=BTC_USD")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
