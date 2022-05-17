N, M = map(int, input().split())

la = [list(map(int, input().split())) for _ in range(N)]
area = 0

# 위, 아래 면
area += N * M * 2

# 오른쪽
for i in range(N):
    for j in range(M):
        if j == 0:
            area += la[i][j]
        else:
            if la[i][j] > la[i][j-1]:
                area += la[i][j] - la[i][j-1]

for i in range(N):
    for j in range(M-1,-1,-1):
        if j == M-1:
            area += la[i][j]
        else:
            if la[i][j] > la[i][j+1]:
                area += la[i][j] - la[i][j+1]

# 왼쪽
for j in range(M):
    for i in range(N):
        if i == 0:
            area += la[i][j]
        else:
            if la[i][j] > la[i-1][j]:
                area += abs(la[i][j] - la[i-1][j])

for j in range(M):
    for i in range(N-1, -1, -1):
        if i == N-1:
            area += la[i][j]
        else:
            if la[i][j] > la[i+1][j]:
                area += abs(la[i][j] - la[i+1][j])

print(area)