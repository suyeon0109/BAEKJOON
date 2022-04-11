dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

N, M, K = map(int, input().split())
# wall -> 격자
wall = [[[] for _ in range(N)] for _ in range(N)]
# balls -> 맨 처음 파이어볼들
balls = [list(map(int, input().split())) for _ in range(M)]

for i in range(M):
    wall[(balls[i][0]-1 + dx[balls[i][4]]*balls[i][3]) % N][(balls[i][1]-1 + dy[balls[i][4]]*balls[i][3]) % N].append(balls[i])

for _ in range(K):
    wall_new = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if wall[i][j]:  # 칸에 파이어볼이 있으면
                if len(wall[i][j]) != 1:  # 파이어볼이 여러개이면

                    for k in range(0,len(wall[i][j])-1):
                        if wall[i][j][k][4]%2 != wall[i][j][k+1][4]%2:  # 파이어볼끼리의 방향이 다 같은 홀짝인지 아닌지 검증
                            t = 1   # -> 추후에 방향 설정에 이용
                            break
                    else:
                        t = 0

                    m_sum = 0   # 질량 합
                    s_sum = 0   # 속력 합
                    for p in wall[i][j]:
                        m_sum += p[2]
                        s_sum += p[3]
                    m_sum //= 5
                    s_sum //= len(wall[i][j])

                    if m_sum != 0:
                        for q in range(t,8,2):
                            # 새로운 벽 wall_new에 이동한 파이어볼 입력
                            wall_new[(i + dx[q]*s_sum) % N][(j + dy[q]*s_sum) % N].append([i,j,m_sum,s_sum,q])

                else: # 칸에 파이어볼이 1개면
                    a = wall[i][j].pop()
                    wall_new[(i + dx[a[4]] * a[3]) % N][(j + dy[a[4]] * a[3]) % N].append(a)

    wall = wall_new  # wall을 wall_new로 교체

ans = 0
for i in range(N):
    for j in range(N):
        if wall[i][j]:
            for k in wall[i][j]:
                ans += k[2]
print(ans)
