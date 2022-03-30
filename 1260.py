from collections import deque
import sys
sys.setrecursionlimit(10**6)

N, M, V = map(int, input().split())
adj = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a,b = map(int, input().split())
    adj[a][b], adj[b][a] = 1, 1


visited = [0]*(N+1)
visited[V] = 1
stk = deque()
stk.append(V)
path = deque()
path.append(V)

def dfs(n):

    for j in range(N+1):
        if adj[n][j] == 1 and visited[j] == 0:
            visited[j] = 1
            path.append(j)
            stk.append(j)
            return dfs(j)
    else:
        stk.pop()
        if stk:
            dfs(stk[-1])
        else:
            return
dfs(V)
print(*path)

visited_B = [0]*(N+1)
visited_B[V] = 1
Q = deque()
Q.append(V)
path_B = deque()

def bfs():
    while Q:
        t = Q.popleft()
        path_B.append(t)
        for k in range(N+1):
            if adj[t][k] == 1 and visited_B[k] == 0:
                Q.append(k)
                visited_B[k] = 1
bfs()
print(*path_B)