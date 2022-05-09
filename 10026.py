from collections import deque

N = int(input())
la = [input() for _ in range(N)]

Q = deque()

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs():
    while Q:
        x,y = Q.popleft()
        for k in range(4):
            a = x + dx[k]
            b = y + dy[k]
            if 0 <= a <= N-1 and 0 <= b <= N-1 and visited[a][b] == 0 and la[a][b] == la[p][q]:
                Q.append((a,b))
                visited[a][b] = 1

cnt = 0
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            p,q = i,j
            Q.append((i,j))
            visited[i][j] = 1
            bfs()
            cnt += 1

for t in range(N):
    la[t] = la[t].replace('G','R')

cnt_2 = 0
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            p,q = i,j
            Q.append((i,j))
            visited[i][j] = 1
            bfs()
            cnt_2 += 1

print(cnt, cnt_2)