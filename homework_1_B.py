from __future__ import annotations


class Ternary:
    num: int

    def __init__(self, num: int) -> None:
        self.num = num

    def __add__(self, other: Ternary) -> Ternary:
        return Ternary(self.num + other.num)

    def __sub__(self, other: Ternary) -> Ternary:
        return Ternary(self.num - other.num)

    def __mul__(self, other: Ternary) -> Ternary:
        return Ternary(self.num * other.num)

    def __floordiv__(self, other: Ternary) -> Ternary:
        return Ternary(self.num // other.num)

    def __str__(self) -> str:
        out = []
        i = self.num
        while i > 0:
            out.append(str(i % 3))
            i //= 3
        return ''.join(out[::-1])


n = Ternary(int(input(), 3))
m = Ternary(int(input(), 3))
print(n + m)
print(n - m)
print(n * m)
print(n // m)
print(n)
