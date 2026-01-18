from multiple_checker import MultipleChecker


class REPLApp:
    STOP_VALUE = -1

    def run(self) -> None:
        print("=== REPL: Multiple Checker (OOP) ===")
        print("Enter two integers each round.")
        print("Type -1 at any prompt to stop.\n")

        while True:
            a = self._read_int("Enter first number (or -1 to stop): ")
            if a == self.STOP_VALUE:
                print("Stopping. Bye!")
                break

            b = self._read_int("Enter second number (or -1 to stop): ")
            if b == self.STOP_VALUE:
                print("Stopping. Bye!")
                break

            result = MultipleChecker.is_multiple(a, b)

            if result:
                print(f"Result: YES — one number is a multiple of the other ({a}, {b}).\n")
            else:
                print(f"Result: NO — neither number is a multiple of the other ({a}, {b}).\n")

    def _read_int(self, prompt: str) -> int:
        while True:
            raw = input(prompt).strip()
            try:
                return int(raw)
            except ValueError:
                print("Error: Please enter a valid integer.")


if __name__ == "__main__":
    REPLApp().run()
