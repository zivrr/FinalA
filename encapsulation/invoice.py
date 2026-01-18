from __future__ import annotations


class Invoice:
    

    def __init__(self, invoice_number: str, customer_name: str, issue_date: str, vat_rate: float) -> None:
        self.customer_name = customer_name  
        self.issue_date = issue_date        

        self.__invoice_number = invoice_number  
        self._vat_rate = 0.0                    
        self.vat_rate = vat_rate                

        self._items: list[dict] = []            
        self._paid: bool = False               



    @property
    def invoice_number(self) -> str:
        return self.__invoice_number

    @property
    def vat_rate(self) -> float:
        return self._vat_rate

    @vat_rate.setter
    def vat_rate(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("VAT rate must be a number (int/float).")
        if value < 0 or value > 1:
            raise ValueError("VAT rate must be between 0 and 1 (e.g., 0.17 for 17%).")
        self._vat_rate = float(value)

    @property
    def is_paid(self) -> bool:
        return self._paid

    @property
    def items(self) -> tuple[dict, ...]:
        return tuple(self._items)

    @property
    def subtotal(self) -> float:
        return self.calculate_subtotal()

    @property
    def vat_amount(self) -> float:
        return round(self.subtotal * self.vat_rate, 2)

    @property
    def total(self) -> float:
        return round(self.subtotal + self.vat_amount, 2)


    def add_item(self, description: str, quantity: int, unit_price: float) -> None:
        if not description.strip():
            raise ValueError("Item description cannot be empty.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        if not isinstance(unit_price, (int, float)) or unit_price <= 0:
            raise ValueError("Unit price must be a positive number.")

        self._items.append(
            {"desc": description.strip(), "qty": quantity, "unit_price": float(unit_price)}
        )

    def calculate_subtotal(self) -> float:
        subtotal = 0.0
        for item in self._items:
            subtotal += item["qty"] * item["unit_price"]
        return round(subtotal, 2)

    def mark_as_paid(self) -> bool:
        if self._paid:
            return False
        self._paid = True
        return True

    def __repr__(self) -> str:
        status = "PAID" if self.is_paid else "UNPAID"
        return (
            f"Invoice(number='{self.invoice_number}', customer='{self.customer_name}', "
            f"date='{self.issue_date}', items={len(self._items)}, "
            f"subtotal={self.subtotal}, vat={self.vat_amount}, total={self.total}, status={status})"
        )
