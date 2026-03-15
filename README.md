# Crypto Service

Проект представляет собой сервис для сбора и хранения актуальных цен криптовалют (BTC и ETH) с биржи Deribit и предоставления этих данных через REST API на FastAPI.

---

## Структура проекта

---

## Установка и запуск

### 1. Клонируем репозиторий и создаем виртуальное окружение

```bash
git clone https://github.com/NikaL25/crypto_service.git
cd crypto_service
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

### 2. Настройка переменных окружения

## Создайте файл .env в корне проекта:

# Application

APP_NAME=crypto_price_service
DEBUG=true

# Database

POSTGRES_HOST=postgres
POSTGRES_PORT=5432
POSTGRES_DB=crypto_db
POSTGRES_USER=crypto_user
POSTGRES_PASSWORD=crypto_password

DATABASE_URL=postgresql://crypto_user:crypto_password@postgres:5432/crypto_db

# Redis

REDIS_HOST=redis
REDIS_PORT=6379

# Celery

CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/1

## 3. Запуск через Docker

`docker-compose up -d --build`

## 4. Применение Миграций Alembic

`docker exec -it crypto_service-api-1 alembic revision --autogenerate -m "create prices table" `

`docker exec -it crypto_service-api-1 alembic upgrade head`

## 5. Проверка создания таблице в базе данных

`docker exec -it crypto_service-postgres-1 psql -U crypto_user -d crypto_db`

`\dt`

# Ожидаемый результат

              List of relations

Schema | Name | Type | Owner
--------+-----------------+-------+-------------
public | alembic_version | table | crypto_user
public | prices | table | crypto_user
(2 rows)

### API Endpoints

# Все методы требуют query-параметр ticker (например, BTC_USD или ETH_USD).

| Метод          | URL               | Описание                                   |
| -------------- | ----------------- | ------------------------------------------ |
| Получить все   | `/prices/all`     | Возвращает все цены по указанной валюте    |
| Последняя цена | `/prices/latest`  | Возвращает последнюю цену по валюте        |
| По дате        | `/prices/by-date` | Возвращает цены в диапазоне UNIX timestamp |

## Design Decisions

# 1. FastAPI — выбран для быстрого и асинхронного API с встроенной документацией Swagger.

# 2. SQLAlchemy + PostgreSQL — для гибкой работы с БД, ORM позволяет легко расширять модель.

# 3. Celery + Redis — для периодического сбора данных с биржи без блокировки основного приложения.

# 4. aiohttp в клиенте Deribit — асинхронные запросы для минимизации задержек при сборе цен.

# 5. Alembic - управление миграциями базы данных.

# 6. Слои архитектуры:

    clients — обращение к внешним API (Deribit).

    services — бизнес-логика и взаимодействие с БД через сервисы.

    api — маршруты FastAPI.

    db — модели и сессии SQLAlchemy.

    workers — Celery tasks для фоновых задач.

# 7. Отсутствие глобальных переменных — все зависимости передаются через Depends и DI (FastAPI + SQLAlchemy).

# 8. Unit тесты — покрытие основных сервисов и API для безопасного рефакторинга.

# 9. Dockerized — проект полностью контейнеризован, что облегчает деплой и настройку окружения.

## Тестирование

` pytest tests/`

## Screenshots

![get-all](screenshots/screen-2.jpg)

![latest](screenshots/screen-2.jpg)

![by-date](screenshots/screen-2.jpg)
