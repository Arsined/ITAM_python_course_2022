def summation(start, end: int) -> int:
    out = 0
    for i in range(min(start, end), max(start, end)+1):
        out += i
    return out


print(summation(2, 12))
print(summation(-4, 4))
print(summation(3, 2))
