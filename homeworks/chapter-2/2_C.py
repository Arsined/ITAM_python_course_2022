def translate(value: int, base: int, alphabet: str) -> str:
    if value == 0:
        return "0"
    out = ['']
    if value < 0:
        out[0] = "-"
        value = abs(value)
    while value > 0:
        out.append(alphabet[value % base])
        value //= base
    return out[0]+''.join(out[:0:-1])


alph = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(translate(2, 2, alph))
print(translate(10, 16, alph))
