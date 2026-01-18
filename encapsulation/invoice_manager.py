from __future__ import annotations
from invoice import Invoice
from customer import Customer


class InvoiceManager:

    def __init__(self, company_name: str) -> None:
        self.company_name = company_name
        self._customers_by_id: dict[str, Customer] = {}        
        self._invoices_by_number: dict[str, Invoice] = {}      

    

    def add_customer(self, customer: Customer) -> None:
        self._customers_by_id[customer.customer_id] = customer

    def get_customer(self, customer_id: str) -> Customer | None:
        return self._customers_by_id.get(customer_id)


    def create_invoice(self, invoice: Invoice, customer_id: str) -> str:
        customer = self.get_customer(customer_id)
        if customer is None:
            return "Error: Customer not found."

        if invoice.invoice_number in self._invoices_by_number:
            return "Error: Invoice number already exists."

        self._invoices_by_number[invoice.invoice_number] = invoice
        customer.add_invoice_number(invoice.invoice_number)
        return "Invoice created successfully."

    def get_invoice(self, invoice_number: str) -> Invoice | None:
        return self._invoices_by_number.get(invoice_number)

    def add_item_to_invoice(self, invoice_number: str, description: str, quantity: int, unit_price: float) -> str:
        invoice = self.get_invoice(invoice_number)
        if invoice is None:
            return "Error: Invoice not found."

        try:
            invoice.add_item(description, quantity, unit_price)
            return "Item added successfully."
        except (ValueError, TypeError) as e:
            return f"Error: {e}"

    def pay_invoice(self, invoice_number: str) -> str:
        invoice = self.get_invoice(invoice_number)
        if invoice is None:
            return "Error: Invoice not found."

        if invoice.mark_as_paid():
            return "Payment successful: Invoice marked as PAID."
        return "Payment skipped: Invoice is already PAID."

    def __repr__(self) -> str:
        return (
            f"InvoiceManager(company='{self.company_name}', "
            f"customers={len(self._customers_by_id)}, invoices={len(self._invoices_by_number)})"
        )
