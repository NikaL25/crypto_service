from celery import Celery
from app.core.config import settings
from celery.schedules import crontab


celery_app = Celery(
    "crypto_worker",
    broker=f"redis://{settings.redis_host}:{settings.redis_port}/0",
    backend=f"redis://{settings.redis_host}:{settings.redis_port}/1",
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)

celery_app.autodiscover_tasks(["app.workers"])


celery_app.conf.beat_schedule = {
    "fetch-prices-every-minute": {
        "task": "app.workers.tasks.fetch_crypto_prices",
        "schedule": crontab(minute="*/1"),
    },
}
