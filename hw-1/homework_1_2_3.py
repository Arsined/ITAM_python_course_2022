str = input()
out=[]
step = 0
for i in range(len(str)):
    if(str[i].isupper() and
        len(out) == 0):
        out.append(str[i])
        step = i
    if(str[i].isdigit() and
        len(out) == 1):
        out.append(str[i+1])
        step = i + 1 - step
        index = i + 1 + step
        break
for i in range(index, len(str), step):
    out.append(str[i])
print(''.join(out))