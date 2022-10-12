arr = map(int, input().split(" "))
negative = 0
greater_than_8 = 0
even = 0
for i in arr:
    if(i < 0):
        negative += 1
    elif(i > 8):
        greater_than_8 += 1
    if(i % 2 == 0):
        even +=1
print(negative, greater_than_8, even)