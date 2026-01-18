from __future__ import annotations
from abc import ABC, abstractmethod


class Security(ABC):
 

    def __init__(self, symbol: str, price: float, quantity: int) -> None:
        self.symbol = symbol
        self.price = price
        self.quantity = quantity

    def market_value(self) -> float:
        return round(self.price * self.quantity, 2)

    @abstractmethod
    def info(self) -> str:
        raise NotImplementedError
