from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

M, N = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

Q = deque()
Q.append((0,0))
visited[0][0] = 1

while Q:
    a, b = Q.popleft()
    n = visited[a][b]
    for i in range(4):
        if 0 <= a + dx[i] <= N-1 and 0 <= b + dy[i] <= M-1:
            if visited[a+dx[i]][b+dy[i]]:
                if maze[a + dx[i]][b + dy[i]] + n < visited[a+dx[i]][b+dy[i]]:
                    visited[a+dx[i]][b+dy[i]] = maze[a + dx[i]][b + dy[i]] + n
                    Q.append((a + dx[i],b + dy[i]))
            else: 
                visited[a+dx[i]][b+dy[i]] = maze[a + dx[i]][b + dy[i]] + n
                Q.append((a + dx[i],b + dy[i]))


print(visited[N-1][M-1]-1)