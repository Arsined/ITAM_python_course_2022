n = int(input())
true_amount = 0
for i in range(n):
    true_amount += 1 if (input().split(" ")[-1] == "True") else 0
print(true_amount, n - true_amount)