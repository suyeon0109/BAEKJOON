from collections import deque
import sys

n = int(sys.stdin.readline())
visited = [0]*(n+1)
stk = deque()
la = deque()
lb = []

stk.append(0)
for _ in range(n):
    lb.append(int(sys.stdin.readline()))

cnt = 1
for m in lb:
    p = cnt

    if visited[m] == 0:
        for j in range(p,m+1):
            visited[cnt] = 1
            stk.append(j)
            la.append('+')
            cnt += 1
            
        stk.pop()
        la.append('-')
    else:
        t = 1
        while stk[-1] >= m:
            stk.pop()
            la.append('-')
            t += 1
        if t == 1:
            print('NO')
            break
else:
    for i in la:
        print(i)