# 4580 ms.....

import sys
dx = [-1,0,1,0]
dy = [0,1,0,-1]
sys.setrecursionlimit(10**6)

def dfs(a):
    global dist
    for j in adj[a]:
        if dist >= 0:
            return

        # 방문한적 없을 때
        if visited[j] == -1:
            visited[j] = visited[a] + 1
            dfs(j)
        else:
            # 방문한 적 있는데, 바로 전 역이 아닐 때 -> 사이클이다 -> 처음 위치에서 마지막 위치 - 1 = 거리
            if visited[j] != visited[a] - 1:
                dist = visited[j] - 1
                dist_lst.append(dist)
                return

N = int(input())
adj = [[] for _ in range(N+1)]

for _ in range(N):
    p,q = map(int, input().split())
    adj[p].append(q)
    adj[q].append(p)

dist_lst = []
for i in range(1,N+1):
    visited = [-1]*(N+1)
    dist = -1
    visited[i]= 1
    dfs(i)

print(*dist_lst)