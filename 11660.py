import sys

N, M = map(int, sys.stdin.readline().split())
matrix = [[0]*(N+1)] + [[0] + list(map(int, sys.stdin.readline().split())) for _ in range(N)]
chk = [[0]*(N+1) for _ in range(N+1)]
ssum = 0

for p in range(N+1):
    for q in range(N+1):
        ssum += matrix[p][q]
        chk[p][q] = ssum

for _ in range(M):
    ssum2 = 0
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    
    for i in range(x1, x2+1):
        ssum2 += chk[i][y2] - chk[i][y1-1]

    print(ssum2)