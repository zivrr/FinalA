from __future__ import annotations


class MultipleChecker:
   

    @staticmethod
    def is_multiple(a: int, b: int) -> bool:
        if a == 0 and b == 0:
            # Usually considered undefined; we choose False for clarity.
            return False

        # If b != 0, check if a is multiple of b
        if b != 0 and (a % b == 0):
            return True

        # If a != 0, check if b is multiple of a
        if a != 0 and (b % a == 0):
            return True

        return False
