import sys
sys.setrecursionlimit(10**9)
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

def dfs(i,j):
    for m in range(8):
        if 0 <= i+dx[m] <= h-1 and 0 <= j+dy[m] <= w-1:
            if mapp[i+dx[m]][j+dy[m]] == 1:
                mapp[i+dx[m]][j+dy[m]] = 0
                dfs(i+dx[m], j+dy[m])
    else:
        return

w, h = map(int, sys.stdin.readline().split())
while w != 0 and h != 0:
    mapp = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    cnt = 0
    for p in range(h):
        for q in range(w):
            if mapp[p][q] == 1:
                mapp[p][q] = 0
                dfs(p,q)
                cnt += 1
    print(cnt)
    w, h = map(int, sys.stdin.readline().split())