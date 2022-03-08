E, S, M = map(int, input().split())
n = 0

def calc(m):
    if (E + 15*n)%m == 0:
        return m
    else:
        return (E + 15*n)%m

while 1:
    if calc(28) == S:
        if calc(19) == M:
            print(E+15*n)
            break
        else:
            n += 1
    else:
        n += 1