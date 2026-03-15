import aiohttp


class DeribitClient:

    BASE_URL = "https://test.deribit.com/api/v2"

    async def get_index_price(
        self,
        ticker: str
    ) -> float:

        url = f"{self.BASE_URL}/public/get_index_price"

        params = {
            "index_name": ticker.lower()
        }

        async with aiohttp.ClientSession() as session:

            async with session.get(
                url,
                params=params,
                timeout=aiohttp.ClientTimeout(total=10)
            ) as response:

                response.raise_for_status()

                data = await response.json()

                return data["result"]["index_price"]
