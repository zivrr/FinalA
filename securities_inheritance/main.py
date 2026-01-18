from stock import Stock
from bond import Bond
from option import Option


def read_non_empty(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: input cannot be empty. Please try again.")


def read_int(prompt: str, min_value: int | None = None) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
            if min_value is not None and val < min_value:
                print(f"Error: value must be >= {min_value}.")
                continue
            return val
        except ValueError:
            print("Error: please enter a valid integer.")


def read_float(prompt: str, min_value: float | None = None) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            val = float(raw)
            if min_value is not None and val < min_value:
                print(f"Error: value must be >= {min_value}.")
                continue
            return val
        except ValueError:
            print("Error: please enter a valid number.")


def main() -> None:
    print("=== Inheritance: Securities System (OOP) ===\n")
    print("Enter required details for a STOCK:")
    s_symbol = read_non_empty("Stock symbol: ")
    s_price = read_float("Stock price: ", min_value=0.0)
    s_qty = read_int("Stock quantity (>= 1): ", min_value=1)
    s_div = read_float("Dividend per share (>= 0): ", min_value=0.0)

    stock = Stock(symbol=s_symbol, price=s_price, quantity=s_qty, dividend_per_share=s_div)

    print("\nEnter required details for a BOND:")
    b_symbol = read_non_empty("Bond symbol: ")
    b_price = read_float("Bond price: ", min_value=0.0)
    b_qty = read_int("Bond quantity (>= 1): ", min_value=1)
    b_coupon = read_float("Coupon rate in percent (e.g., 5 for 5%): ", min_value=0.0)

    bond = Bond(symbol=b_symbol, price=b_price, quantity=b_qty, coupon_rate=b_coupon)

    print("\nEnter required details for an OPTION:")
    o_symbol = read_non_empty("Option symbol: ")
    o_price = read_float("Option price (premium): ", min_value=0.0)
    o_qty = read_int("Option quantity (>= 1): ", min_value=1)
    o_strike = read_float("Strike price: ", min_value=0.0)
    o_type = read_non_empty("Option type (call/put): ").lower().strip()

    option = Option(symbol=o_symbol, price=o_price, quantity=o_qty, strike_price=o_strike, option_type=o_type)
    underlying_price = read_float("\nEnter underlying price (for option intrinsic value calculation): ", min_value=0.0)

    print("\n---- Created Objects (info()) ----")
    print(stock.info())
    print(bond.info())
    print(option.info())
    print("\n---- Calling Methods ----")
    print(f"Stock market value: {stock.market_value():.2f}")
    print(f"Stock annual dividend income: {stock.annual_dividend_income():.2f}")
    print(f"\nBond market value: {bond.market_value():.2f}")
    print(f"Bond annual coupon payment: {bond.annual_coupon_payment():.2f}")
    print(f"\nOption market value (premium * quantity): {option.market_value():.2f}")
    print(f"Option intrinsic value (total): {option.intrinsic_value(underlying_price):.2f}")
    print("\nDone.")


if __name__ == "__main__":
    main()
#סעיף 2 - ד :

#מטרת ההורשה :
#לאפשר יצירת מחלקות “בן” שמקבלות (יורשות) את התכונות וההתנהגויות המשותפות ממחלקת “אב”, וכך:
#1.	מונעים כפילות קוד - לא צריך לכתוב שוב ושוב.
#2.	יוצרים מבנה היררכי ברור: ״נייר ערך״ הוא מושג כללי, ומניה/אג״ח/אופציה הם סוגים ספציפיים שלו.
#3.	מאפשרים הרחבה: כל סוג מוסיף תכונה/מתודה ייחודית בלי לשבור את הבסיס.
#התוצאה בפועל בקוד:
#1. •	יש מחלקת אב Security  עם מאפיינים משותפים (symbol, price, quantity) ומתודה כללית market_value().
#2  •	שלוש מחלקות יורשות (Stock, Bond, Option) מקבלות את המשותף אוטומטית, ומוסיפות כל אחת:
#א. o	מניה: dividend_per_share + מתודה annual_dividend_income()
#ב. o	אג״ח: coupon_rate + מתודה annual_coupon_payment()
#ג. o	אופציה: strike_price + option_type + מתודה intrinsic_value()
#•	ב־ main אנחנו קולטים נתונים,
#  יוצרים מופעים מכל הסוגים, וקוראים גם למתודה המשותפת 
# (market_value) וגם למתודות הייחודיות — וזה מדגים הורשה בצורה ברורה.

