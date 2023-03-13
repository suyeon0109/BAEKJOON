import sys
from collections import deque

def bfs():
    while loc:
        a,b = loc.popleft()
        for k in range(4):
            X = a + dx[k]
            Y = b + dy[k]
            if 0 <= X <= N-1 and 0 <= Y <= M-1 and visited[X][Y] == 0 and cabbage[X][Y] == 1:
                loc.append((X,Y))
                visited[X][Y] = 1

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for _ in range(int(input())):
    M, N, K = map(int, sys.stdin.readline().split())
    cabbage = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    cnt = 0

    loc = deque()

    for _ in range(K):
        a,b = map(int, sys.stdin.readline().split())
        cabbage[b][a] = 1
    
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and cabbage[i][j] == 1:
                loc.append((i,j))
                bfs()
                cnt += 1
    
    print(cnt)