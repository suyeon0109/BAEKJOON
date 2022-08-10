import sys

R, C = map(int, sys.stdin.readline().split())

la = [list(map(str, sys.stdin.readline())) for _ in range(R)]
visited = [0]*26

dx = [0,1,0,-1]
dy = [1,0,-1,0]
visited[ord(la[0][0])-65] = 1

cnt = 1
cnt_max = 0
def dfs(a,b):
    global cnt, cnt_max
    for k in range(4):
        A = a + dx[k]
        B = b + dy[k]
        if 0 <= A <= R-1 and 0 <= B <= C-1 and not visited[ord(la[A][B])-65]:
            visited[ord(la[A][B])-65] = 1
            cnt += 1
            dfs(A, B)
    else:
        if cnt_max < cnt:
            cnt_max = cnt
        cnt -= 1
        visited[ord(la[a][b])-65] = 0
        return

dfs(0,0)

print(cnt_max)