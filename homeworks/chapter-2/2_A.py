def ladder(n: int) -> int:
    out = 0
    i = 1
    while i <= n:
        out += 1
        i += out + 1
    return out


print(ladder(3))
print(ladder(6))
# Я вообще не понял задание, считаю на каждой ступени + 1
