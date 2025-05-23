from pydantic import BaseModel
from app.models.trade_request import TradeStatus
from typing import Literal, Optional

class TradeRequestBase(BaseModel):
    symbol: str
    name: Optional[str] = None
    quantity: int
    price: float
    trade_type: Literal["buy", "sell"]

class TradeRequestCreate(TradeRequestBase):
    pass

class TradeRequestOut(TradeRequestBase):
    id: int
    user_id: int
    status: TradeStatus

    class Config:
        orm_mode = True