la = [i for i in range(10001)]

def selfnum(n):
    num = 0
    num += n
    n = str(n)
    for i in n:
        num += int(i)
    if num > 10000:
        return
    la[num] = 0
    return selfnum(num)

for j in range(len(la)):
    if la[j] != 0:
        selfnum(j)

for i in range(10001):
    if la[i] != 0:
        print(la[i])