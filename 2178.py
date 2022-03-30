def maze():
    while Q:

        I,J = Q.pop(0)
        t = visited[I][J]

        for k in range(4):
            try:
                if I+dx[k]>=0 and J+dy[k]>=0:

                    if la[I+dx[k]][J+dy[k]] == 1 and visited[I+dx[k]][J+dy[k]] == 0:
                        Q.append((I+dx[k],J+dy[k]))
                        visited[I+dx[k]][J+dy[k]] = t+1

                        if I+dx[k] == N-1 and J+dy[k] == M-1:
                            return visited[I+dx[k]][J+dy[k]]
            except:
                pass
    else:
        return 0


N,M = map(int, input().split())
la = [list(map(int, input())) for _ in range(N)]
Q = []
visited = [[0]*M for _ in range(N)]

I,J = 0,0
visited[I][J] = 1
Q.append((I,J))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

print(maze())