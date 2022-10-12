n = int(input())
true_amount = 0
false_amount = 0
for i in range(n):
    inp = input()
    if ("True" in inp.split(" ")):
        if("False" not in inp.split(" ") or
            inp.split(" ")[-1] == "True"):
            true_amount += 1
        elif(inp.split(" ")[-1] == "False"):
            false_amount += 1
print(true_amount, false_amount, n - true_amount - false_amount)