def greetings(line: str) -> str:
    out = line.split()
    return f"Доброго времени суток, {out[0]} \"Человек\" {out[1]}!"


print(greetings("Гендо Геннадий"))
