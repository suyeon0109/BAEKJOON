from collections import deque
import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
adj = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adj[a][b] , adj[b][a] = 1,1

visited = [0]*(N+1)
stk = deque()
cnt = 0

def dfs(n):
    for i in range(N+1):
        if adj[n][i] == 1 and visited[i] == 0:
            visited[i] = 1
            stk.append(i)
            return dfs(i)
    else:
        stk.pop()
        if stk:
            dfs(stk[-1])
        else:
            return

for k in range(1,N+1):
    if visited[k] == 0:
        visited[k] = 1
        stk.append(k)
        dfs(k)
        cnt += 1

print(cnt)
    