from datetime import datetime
from sqlalchemy import String, Float, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base


class Price(Base):
    __tablename__ = "prices"

    id: Mapped[int] = mapped_column(primary_key=True)
    ticker: Mapped[str] = mapped_column(String(20), index=True)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    timestamp: Mapped[datetime] = mapped_column(TIMESTAMP, index=True)

    def __repr__(self) -> str:
        return f"<Price ticker={self.ticker} price={self.price} timestamp={self.timestamp}>"
