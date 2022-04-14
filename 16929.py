dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dfs(a,b):
    global success
    for k in range(4):
        x = a+dx[k]
        y = b+dy[k]
        if 0 <= x <= N-1 and 0 <= y <= M-1 and dots[a][b] == dots[x][y]:

            # 다음 칸의 visit = 원래칸의 visit + 1
            if visited[x][y] == -1:
                visited[x][y] = visited[a][b]+1
                dfs(x,y)
            
            # 만약 다음칸이 visited 이며 원래칸의 바로 전칸이 아니라면 -> 사이클!
            elif visited[x][y] != visited[a][b] - 1:
                success = 'Yes'
                return 


N, M = map(int, input().split())
dots = [list(map(str, input())) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]
success = 'No'

for i in range(N):
    for j in range(M):
        if visited[i][j] == -1:
            visited[i][j] = 1
            dfs(i,j)
            if success == 'Yes':
                break
    if success == 'Yes':
        break

print(success)