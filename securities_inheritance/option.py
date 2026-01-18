from __future__ import annotations
from security import Security


class Option(Security):
  

    def __init__(self, symbol: str, price: float, quantity: int, strike_price: float, option_type: str) -> None:
        super().__init__(symbol, price, quantity)
        self.strike_price = strike_price
        self.option_type = option_type.lower().strip()  

    def intrinsic_value(self, underlying_price: float) -> float:
        if self.option_type == "call":
            per_unit = max(0.0, underlying_price - self.strike_price)
        elif self.option_type == "put":
            per_unit = max(0.0, self.strike_price - underlying_price)
        else:
            raise ValueError("option_type must be 'call' or 'put'.")
        return round(per_unit * self.quantity, 2)

    def info(self) -> str:
        return (
            f"Option(symbol={self.symbol}, price={self.price}, quantity={self.quantity}, "
            f"strike_price={self.strike_price}, type={self.option_type})"
        )
