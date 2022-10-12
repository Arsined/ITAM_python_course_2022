class NumerialSystem:
    num_2 = []
    num_3 = []

    def __init__(self, num: list) -> None:
        self.num_2 = []
        self.num_3 = []
        for i in num:
            if i[0] == "BINARY":
                self.num_2.append(i[1])
            elif i[0] == "TERNARY":
                self.num_3.append(i[1])

    def sortt(self) -> str:
        self.num_2.sort()
        self.num_3.sort()
        j = 0
        out = ""
        for i in range(len(self.num_2)):
            while j < len(self.num_3):
                if int(str(self.num_3[j]), 3) < int(str(self.num_2[i]), 2):
                    out += str(self.num_3[j]) + " "
                    j += 1
                else:
                    break
            out += str(self.num_2[i]) + " "
        out += " ".join(map(str, self.num_3[j:]))
        return out


array = [
        ["TERNARY", 221],
        ["BINARY", 101010],
        ["BINARY", 10000],
        ["TERNARY", 222],
        ["TERNARY", 12100],
        ["TERNARY", 20201],
        ["TERNARY", 21],
        ["BINARY", 10]
    ]
cls = NumerialSystem(array)
print(cls.sortt())

array = []
for _ in range(int(input())):
    array.append(input().split())
cls = NumerialSystem(array)
print(cls.sortt())
