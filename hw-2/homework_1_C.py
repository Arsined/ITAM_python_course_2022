def summation(*args: int) -> int:
    help_list = [abs(i) * 2 if i < 0 else i for i in args]
    out = 0
    maxx = max(help_list)
    for i in help_list:
        i /= maxx
        out += i
    return out


print(summation(-10, 2, 3, 15, -4))
