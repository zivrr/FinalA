from __future__ import annotations
from security import Security


class Bond(Security):


    def __init__(self, symbol: str, price: float, quantity: int, coupon_rate: float) -> None:
      
        super().__init__(symbol, price, quantity)
        self.coupon_rate = coupon_rate

    def annual_coupon_payment(self) -> float:
        rate = self.coupon_rate / 100.0
        return round(self.market_value() * rate, 2)

    def info(self) -> str:
        return (
            f"Bond(symbol={self.symbol}, price={self.price}, quantity={self.quantity}, "
            f"coupon_rate={self.coupon_rate}%)"
        )
