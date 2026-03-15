from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str
    debug: bool

    # Postgres
    postgres_host: str
    postgres_port: int
    postgres_db: str
    postgres_user: str
    postgres_password: str

    # Redis
    redis_host: str
    redis_port: int

    # URL
    database_url: str
    celery_broker_url: str
    celery_result_backend: str

    class Config:
        extra = "forbid"
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
