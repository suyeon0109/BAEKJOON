from collections import deque


M, N, K = map(int, input().split())
paper = [[0]*N for _ in range(M)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

Q = deque()

def bfs():
    global cnt
    while Q:
        p,q = Q.popleft()
        for k in range(4):
            a = p + dx[k]
            b = q + dy[k]
            if 0 <= a <= M-1 and 0 <= b <= N-1 and paper[a][b] == 0:
                Q.append((a,b))
                paper[a][b] = 1
                cnt += 1

space = []

for _ in range(K):
    y1,x1,y2,x2 = map(int, input().split())

    for i in range(x1,x2):
        for j in range(y1,y2):
            paper[i][j] = 1

for i in range(M):
    for j in range(N):
        cnt = 0
        if paper[i][j] == 0:
            cnt += 1
            paper[i][j] = 1
            Q.append((i,j))
            bfs()
            space.append(cnt)

space.sort()
print(len(space))
print(*space)