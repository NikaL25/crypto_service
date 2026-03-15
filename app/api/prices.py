from typing import List

from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db_session
from app.repositories.price_repository import PriceRepository
from app.services.price_service import PriceService
from app.schemas.price import PriceResponse


router = APIRouter(prefix="/prices", tags=["prices"])


def get_service(
    session: AsyncSession = Depends(get_db_session)
) -> PriceService:

    repo = PriceRepository(session)

    return PriceService(repo)


@router.get("/all", response_model=List[PriceResponse])
async def get_all_prices(
    ticker: str = Query(...),
    service: PriceService = Depends(get_service),
):

    prices = await service.get_all_prices(ticker)

    return [
        PriceResponse(
            ticker=p.ticker,
            price=p.price,
            timestamp=int(p.timestamp.timestamp()),
        )
        for p in prices
    ]


@router.get("/latest", response_model=PriceResponse)
async def get_latest_price(
    ticker: str = Query(...),
    service: PriceService = Depends(get_service),
):

    price = await service.get_latest_price(ticker)

    if not price:
        raise HTTPException(
            status_code=404,
            detail="Price not found"
        )

    return PriceResponse(
        ticker=price.ticker,
        price=price.price,
        timestamp=int(price.timestamp.timestamp()),
    )


@router.get("/by-date", response_model=List[PriceResponse])
async def get_prices_by_date(
    ticker: str = Query(...),
    date_from: int = Query(...),
    date_to: int = Query(...),
    service: PriceService = Depends(get_service),
):

    prices = await service.get_prices_by_date(
        ticker,
        date_from,
        date_to,
    )

    return [
        PriceResponse(
            ticker=p.ticker,
            price=p.price,
            timestamp=int(p.timestamp.timestamp()),
        )
        for p in prices
    ]
