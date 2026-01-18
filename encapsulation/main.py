from invoice import Invoice
from customer import Customer
from invoice_manager import InvoiceManager


def read_non_empty(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: Input cannot be empty. Please try again.")


def read_int(prompt: str, min_value: int | None = None) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
            if min_value is not None and val < min_value:
                print(f"Error: Value must be >= {min_value}.")
                continue
            return val
        except ValueError:
            print("Error: Please enter a valid integer.")


def read_float(prompt: str, min_value: float | None = None) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            val = float(raw)
            if min_value is not None and val < min_value:
                print(f"Error: Value must be >= {min_value}.")
                continue
            return val
        except ValueError:
            print("Error: Please enter a valid number.")


def main() -> None:
    print("=== Invoice System (Encapsulation / OOP) ===\n")

    
    print("Enter the required details for the company:")
    company_name = read_non_empty("Company name: ")
    manager = InvoiceManager(company_name)

    
    print("\nEnter the required details for the customer:")
    customer_id = read_non_empty("Customer ID: ")
    customer_name = read_non_empty("Customer full name: ")

    customer = Customer(customer_id, customer_name)
    manager.add_customer(customer)  

    
    print("\nEnter the required details for the invoice:")
    invoice_number = read_non_empty("Invoice number (unique): ")
    issue_date = read_non_empty("Issue date (e.g., 2026-01-17): ")
    vat_rate_percent = read_float("VAT rate in percent (e.g., 17 for 17%): ", min_value=0)

    vat_rate = vat_rate_percent / 100.0
    invoice = Invoice(
        invoice_number=invoice_number,
        customer_name=customer.full_name,
        issue_date=issue_date,
        vat_rate=vat_rate,
    )

    create_msg = manager.create_invoice(invoice, customer_id)  
    print(f"\n{create_msg}")
    if create_msg != "Invoice created successfully.":
        print("Stopping because invoice could not be created.")
        return

    
    print("\nEnter invoice items:")
    items_count = read_int("How many items would you like to add? (>= 1): ", min_value=1)

    for i in range(items_count):
        print(f"\nItem #{i + 1}")
        desc = read_non_empty("Description: ")
        qty = read_int("Quantity (positive integer): ", min_value=1)
        unit_price = read_float("Unit price (positive number): ", min_value=0.01)

        
        msg = manager.add_item_to_invoice(invoice_number, desc, qty, unit_price)
        print(msg)

   
    print("\n---- Invoice Summary ----")
    saved_invoice = manager.get_invoice(invoice_number)
    if saved_invoice is None:
        print("Error: Invoice not found after creation (unexpected).")
        return

    print(saved_invoice)

    print("\nItems (read-only view):")
    for idx, item in enumerate(saved_invoice.items, start=1):
        line_total = item["qty"] * item["unit_price"]
        print(f"{idx}. {item['desc']} | qty={item['qty']} | unit_price={item['unit_price']:.2f} | line_total={line_total:.2f}")

    print(f"\nSubtotal: {saved_invoice.subtotal:.2f}")
    print(f"VAT ({saved_invoice.vat_rate * 100:.2f}%): {saved_invoice.vat_amount:.2f}")
    print(f"Total: {saved_invoice.total:.2f}")
    print(f"Status: {'PAID' if saved_invoice.is_paid else 'UNPAID'}")

    
    print("\nEnter the required details for payment:")
    pay_choice = read_non_empty("Would you like to mark the invoice as PAID? (yes/no): ").lower()

    if pay_choice in ("yes", "y"):
       
        print(manager.pay_invoice(invoice_number))
    else:
        print("Payment skipped by user choice.")

   
    print("\n---- Final State ----")
    print(saved_invoice)
    print(customer)
    print("Customer invoices (read-only):", customer.invoice_numbers)



if __name__ == "__main__":
    main()
#:סעיף 1 - ג

#מטרת הכימוס היא להגן על הנתונים הפנימיים של האובייקט ולמנוע גישה או שינוי ישיר ולא מבוקר שלהם מבחוץ.
#  במקום שכל חלק בתוכנית יוכל לשנות ערכים איך שהוא רוצה, הכימוס גורם לכך שהגישה לנתונים תתבצע דרך ממשק מבוקר 
# (מתודות ו־@property) שמוודא שהמידע נשאר תקין והאובייקט לא נכנס למצבים לא הגיוניים.
#במערכת החשבוניות שכתבנו,
#  הכימוס מתבטא בכך שלא מאפשרים לשנות נתונים קריטיים של חשבונית בצורה חופשית. לדוגמה, מספר החשבונית 
# (__invoice_number) מוגדר כ־private,  ולכן אי אפשר לגשת אליו ישירות מחוץ למחלקה או לשנות אותו בטעות. 
# בנוסף, יש תכונות שמוגדרות כ־protected  כמו  (_items, _vat_rate, _paid)
#  שמיועדות לשימוש פנימי של המחלקה ולא אמורות להשתנות ישירות על ידי קוד חיצוני.

