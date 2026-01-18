from __future__ import annotations


class Customer:
    """
    Customer object:
    - Stores invoices by invoice number (protected list)
    - Exposes read-only access via property
    """

    def __init__(self, customer_id: str, full_name: str) -> None:
        self.customer_id = customer_id  
        self.full_name = full_name      
        self._invoice_numbers: list[str] = []  

    @property
    def invoice_numbers(self) -> tuple[str, ...]:
        """Read-only view to prevent external mutation."""
        return tuple(self._invoice_numbers)

    def add_invoice_number(self, invoice_number: str) -> None:
        self._invoice_numbers.append(invoice_number)

    def __repr__(self) -> str:
        return f"Customer(id='{self.customer_id}', name='{self.full_name}', invoices={len(self._invoice_numbers)})"
