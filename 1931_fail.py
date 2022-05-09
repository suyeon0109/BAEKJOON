from collections import deque
import sys
sys.setrecursionlimit(10**9)

N = int(input())
la = deque()
max_val = 0
max_len = 0

for _ in range(N):
    s,e = map(int, sys.stdin.readline().split())
    if s > max_val:
        max_val = s
    if e > max_val:
        max_val = e
    la.append((s,e))

visited = [0] * (max_val + 1)
ans = deque()

def dfs(a):
    global max_len
    for l in range(la[a][0], la[a][1]+1):
        if visited[l] == 1:
            if a < N-1:
                dfs(a+1)
                return
            elif a == N-1:
                if len(ans) > max_len:
                    max_len = len(ans)
                return
    else:
        ans.append(la[a])
        for l in range(la[a][0], la[a][1]+1):
            visited[l] = 1
        if a < N-1:
            dfs(a+1)
        elif a == N-1:
            if len(ans) > max_len:
                max_len = len(ans)
            return

        for l in range(la[a][0], la[a][1]+1):
            visited[l] = 0
        ans.pop()

dfs(0)

print(max_len)