R, C = map(int, input().split())

alpha = [list(map(str, input())) for _ in range(R)]
max_l = 0

dx = [-1,0,1,0]
dy = [0,1,0,-1]


def dfs(a,b):
    global max_l

    t = visited[ord(alpha[i][j])-65]
    print('시작',i,j,alpha[i][j])
    for k in range(4):
        x = a+dx[k]
        y = b+dy[k]
        if 0 <= x <= R-1 and 0 <= y <= C-1 and visited[ord(alpha[x][y])-65] == 0:
            visited[ord(alpha[x][y])-65] = t + 1
            if visited[ord(alpha[x][y])-65] > max_l:
                max_l = visited[ord(alpha[x][y])-65]
                print(alpha[x][y])
            dfs(x,y)
            visited[ord(alpha[x][y])-65] = 0

for i in range(R):
    for j in range(C):
        visited = [0]*26
        visited[ord(alpha[i][j])-65] = 1
        dfs(i,j)

print(max_l)