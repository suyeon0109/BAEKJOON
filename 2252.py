from collections import deque
import sys

N, M = map(int, input().split())

line = [[] for _ in range(N+1)]
cnt = [0] * (N+1)
Q = deque()
R = deque()

for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())

    line[a].append(b)
    cnt[b] += 1

for i in range(1,N+1):
    if cnt[i] == 0:
        Q.append(i)
        cnt[i] = -1

while Q:

    t = Q.popleft()
    R.append(t)

    for k in line[t]:
        cnt[k] -= 1
        if cnt[k] == 0:
            Q.append(k)
            cnt[k] = -1


print(*R)