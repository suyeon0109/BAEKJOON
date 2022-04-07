dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

N, M, K = map(int, input().split())
wall = [[[] for _ in range(N)] for _ in range(N)]
balls = [list(map(int, input().split())) for _ in range(M)]

for i in range(M):
    wall[(balls[i][0]-1 + dx[balls[i][4]]*balls[i][3]) % N][(balls[i][1]-1 + dy[balls[i][4]]*balls[i][3]) % N].append(balls[i])

for _ in range(K):
    wall_new = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if wall[i][j]:
                if len(wall[i][j]) != 1:

                    for k in range(0,len(wall[i][j])-1):
                        if wall[i][j][k][4]%2 != wall[i][j][k+1][4]%2:
                            t = 1
                            break
                    else:
                        t = 0

                    m_sum = 0
                    s_sum = 0
                    for p in wall[i][j]:
                        m_sum += p[2]
                        s_sum += p[3]
                    m_sum //= 5
                    s_sum //= len(wall[i][j])
                    if m_sum != 0:
                        for q in range(t,8,2):
                            wall_new[(i + dx[q]*s_sum) % N][(j + dy[q]*s_sum) % N].append([i,j,m_sum,s_sum,q])

                else:
                    a = wall[i][j].pop()
                    wall_new[(i + dx[a[4]] * a[3]) % N][(j + dy[a[4]] * a[3]) % N].append(a)
    wall = wall_new
ans = 0
for i in range(N):
    for j in range(N):
        if wall[i][j]:
            for k in wall[i][j]:
                ans += k[2]
print(ans)
