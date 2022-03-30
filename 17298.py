from collections import deque

n = int(input())
la = [0] + list(map(int, input().split()))
stk = deque()
lc = [0]*(len(la))

stk.append(1)
for i in range(2,len(la)):
    if la[i] <= la[i-1]:
        stk.append(i)
    else:
        while stk:
            a = stk.pop()
            if la[i] > la[a]:
                lc[a] = la[i]
            else:
                stk.append(a)
                break
        stk.append(i)

if stk:
    for j in stk:
        lc[j] = -1
lc.pop(0)
print(*lc)