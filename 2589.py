from collections import deque


S, G = map(int, input().split())
mapp = [list(map(str, input())) for _ in range(S)]
Q = deque()
max_l = 0

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs():

    global max_l

    while Q:
        a,b = Q.popleft()
        t = visited[a][b]
        for i in range(4):
            x = a+dx[i]
            y = b+dy[i]
            if 0 <= x <= S-1 and 0 <= y <= G-1 and visited[x][y] == -1 and mapp[x][y] == 'L':
                visited[x][y] = t + 1
                Q.append((x,y))
                if visited[x][y] > max_l :
                    max_l = visited[x][y]


for i in range(S):
    for j in range(G):
        if mapp[i][j] == 'L':
            visited = [[-1]*G for _ in range(S)]
            Q = deque()

            visited[i][j] = 0
            Q.append((i,j))

            bfs()

print(max_l)