from fastapi import FastAPI
from app.api.prices import router as prices_router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
)

app.include_router(prices_router)


@app.get("/health")
async def health_check():
    return {"status": "ok"}
