N, M = map(int, input().split())

la = [[0]*(M+1)] +[[0] + list(map(int, input())) for _ in range(N)]
lb = [[0]*(M+1) for _ in range(N+1)]

dx = [-1,-1,0]
dy = [0,-1,-1]

max_val = 0

for i in range(1,N+1):
    for j in range(1,M+1):
        if la[i][j] == 1:
            for k in range(3):
                p = i + dx[k]
                q = j + dy[k]
                if lb[p][q] == 0:
                    lb[i][j] = 1
                    if max_val < lb[i][j]:
                        max_val = lb[i][j]
                    break
            else:
                lb[i][j] = min(lb[i+dx[0]][j+dy[0]], lb[i+dx[1]][j+dy[1]], lb[i+dx[2]][j+dy[2]]) + 1
                if max_val < lb[i][j]:
                    max_val = lb[i][j]

print(max_val**2)