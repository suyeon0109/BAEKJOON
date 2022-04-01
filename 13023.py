from collections import deque
import sys

def dfs(i):
    global correct, dpt
    for k in range(len(adj[i])):
        if dpt == 5:
            correct = 1
            return
        if visited[adj[i][k]] == 0:
            visited[adj[i][k]] = 1
            dpt += 1
            dfs(adj[i][k])
    else:
        dpt -= 1
        visited[i] = 0
        return

N, M = map(int, sys.stdin.readline().split())
adj = deque()
for _ in range(N):
    adj.append([])
for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)
visited = [0] * N
correct = 0

for p in range(N):
    if sum(adj[p]) != 0 and visited[p] == 0:
        visited[p] = 1
        dpt = 1
        dfs(p)
        if correct == 1:
            print(1)
            break
else:
    print(0)