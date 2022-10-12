from __future__ import annotations


class Binary:
    num: int

    def __init__(self, num: int) -> None:
        self.num = num

    def __add__(self, other: Binary) -> Binary:
        return Binary(self.num + other.num)

    def __sub__(self, other: Binary) -> Binary:
        return Binary(self.num - other.num)

    def __mul__(self, other: Binary) -> Binary:
        return Binary(self.num * other.num)

    def __floordiv__(self, other: Binary) -> Binary:
        return Binary(self.num // other.num)

    def __str__(self) -> str:
        return bin(self.num)[2:]


n = Binary(int(input(), 2))
m = Binary(int(input(), 2))
print(n + m + m)
print(n - m + n)
print(n * m)
print(n // m)
print(n)
