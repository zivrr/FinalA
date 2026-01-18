from __future__ import annotations
from security import Security


class Stock(Security):
 

    def __init__(self, symbol: str, price: float, quantity: int, dividend_per_share: float) -> None:
        super().__init__(symbol, price, quantity)
        self.dividend_per_share = dividend_per_share

    def annual_dividend_income(self) -> float:
        return round(self.dividend_per_share * self.quantity, 2)

    def info(self) -> str:
        return (
            f"Stock(symbol={self.symbol}, price={self.price}, quantity={self.quantity}, "
            f"dividend_per_share={self.dividend_per_share})"
        )
