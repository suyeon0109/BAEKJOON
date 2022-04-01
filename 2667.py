import sys
sys.setrecursionlimit(10**9)
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def dfs(i,j):
    global cnt
    if 0 <= i <= N-1 and 0 <= j <= N-1:
        if house[i][j] == 1:
            house[i][j] = 0
            cnt += 1
        else:
            return
    else:
        return
    
    dfs(i+dx[0], j+dy[0])
    dfs(i+dx[1], j+dy[1])
    dfs(i+dx[2], j+dy[2])
    dfs(i+dx[3], j+dy[3])


N = int(sys.stdin.readline())
house = [list(map(int, input())) for _ in range(N)]
dangi = 0
house_cnt = []

for p in range(N):
    for q in range(N):
        if house[p][q] == 1:
            cnt = 0
            dangi += 1
            dfs(p,q)
            house_cnt.append(cnt)
house_cnt.sort()
print(dangi)
for k in house_cnt:
    print(k)