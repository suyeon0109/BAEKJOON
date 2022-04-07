# dx, dy -> 이동 위치 기준에서, 흩어지는 모래의 비율의 위치(왼,아래,오른,위 방향 순. 퍼센트 오름차순)
# prst -> 모래의 비율 
# x,y -> 이동 위치의 이동 방향

dx = [[-1,1,-2,2,0,-1,1,-1,1,0],[-1,-1,0,0,2,0,0,1,1,1],[-1,1,-2,2,0,-1,1,-1,1,0],[1,1,0,0,-2,0,0,-1,-1,-1]]
dy = [[1,1,0,0,-2,0,0,-1,-1,-1],[-1,1,-2,2,0,-1,1,-1,1,0],[-1,-1,0,0,2,0,0,1,1,1],[-1,1,-2,2,0,-1,1,-1,1,0]]
prst = [0.01,0.01,0.02,0.02,0.05,0.07,0.07,0.1,0.1]
x = [0,1,0,-1]
y = [-1,0,1,0]


N = int(input())
grnd = [list(map(int, input().split())) for _ in range(N)]
a,b = N//2, N//2

# sand -> 격자 밖으로 나가는 모래의 양
sand = 0

# cnt -> 토네이도의 이동 방향을 전환해주기 위한 지표. 4로 나눈 나머지로 이용.
# ex) cnt = 1 -> cnt%4 = 1 -> a + x[cnt] -> a + x[1] -> a + 1
# ex) cnt = 7 -> cnt%4 = 3 -> a + x[cnt] -> a + x[3] -> a - 1
cnt = 0

for i in range(1,N):
    for _ in range(2):
        for _ in range(i):
            a, b = a+x[cnt], b+y[cnt]
            # minus -> 날아간 모래들의 총량
            minus = 0

            # 이동 위치에 모래가 없으면 무시하고 다음 반복.
            if grnd[a][b] == 0:
                continue

            for j in range(9):
                # 이동 위치에 모래가 있고 격자 내로 날아가면, 날아간 위치에 모래 더해준다.
                if 0 <= a+dx[cnt][j] <= N-1 and 0 <= b+dy[cnt][j] <= N-1:
                    grnd[a+dx[cnt][j]][b+dy[cnt][j]] += int(grnd[a][b] * prst[j])
                else:
                    # 격자 밖으로 날아가면 sand에 더해줌
                    sand += int(grnd[a][b] * prst[j])
                
                minus += int(grnd[a][b] * prst[j])
            
            # 원래의 모래양에서 날아간 모래양을 뺀 값을, 알파 자리에 더해줌. (격자 밖으로 나가면 sand에 더해줌)
            if 0 <= a+dx[cnt][9] <= N-1 and 0 <= b+dy[cnt][9] <= N-1 :
                grnd[a+dx[cnt][9]][b+dy[cnt][9]] += grnd[a][b] - minus
            else:
                sand += grnd[a][b] - minus
                
            # 모래가 전부 옮겨졌으므로 모래양 0으로 초기화
            grnd[a][b] = 0
        cnt += 1
        cnt %= 4

# 맨 마지막 왼쪽으로 N-1번 이동하는 부분의 코드.
for _ in range(N-1):
    minus = 0
    a, b = a+x[cnt], b+y[cnt]
    if grnd[a][b] == 0:
        continue
    for j in range(9):
        if 0 <= a+dx[cnt][j] <= N-1 and 0 <= b+dy[cnt][j] <= N-1:
            grnd[a+dx[cnt][j]][b+dy[cnt][j]] += int(grnd[a][b] * prst[j])
        else:
            sand += int(grnd[a][b] * prst[j])
        minus += int(grnd[a][b] * prst[j])
    if 0 <= a+dx[cnt][9] <= N-1 and 0 <= b+dy[cnt][9] <= N-1 :
        grnd[a+dx[cnt][9]][b+dy[cnt][9]] += grnd[a][b] - minus
    else:
        sand += grnd[a][b] - minus
    grnd[a][b] = 0

print(sand)