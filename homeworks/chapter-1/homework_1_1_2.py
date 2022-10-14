arr=input().split(" ")
min=arr[0]
max=arr[0]
for i in arr:
    if(max < i):
        max = i
    if(min > i):
        min = i
print(min, max)