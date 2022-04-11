from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs():
    global cnt_ice
    while Q:
        q = Q.popleft()
        cnt_ice += 1
        for i in range(4):
            if 0 <= q[0]+dx[i] <= M-1 and 0 <= q[1]+dy[i] <= M-1:
                if ice[q[0]+dx[i]][q[1]+dy[i]]:
                    Q.append((q[0]+dx[i], q[1]+dy[i]))
                    ice[q[0]+dx[i]][q[1]+dy[i]] = 0

N, Q = map(int, input().split())
M = 2**N
ice = [list(map(int, input().split())) for _ in range(M)]
# L 리스트
L = list(map(int, input().split()))


# 마법 시전 부분
for z in range(Q):

    # 배열 회전
    t = 0
    p = 0
    n = 2**L[z]
    for _ in range(M//n): 
        for _ in range(M//n):
            r = 0
            for i in range(p,p+n//2): 
                c = n-1-2*(i%n)
                for j in range(t+i%n,t+n-1-i%n): 
                    ice[i][j], ice[i+r][j+c], ice[i+r+c][j+c-r], ice[i+c][j-r] = ice[i+c][j-r], ice[i][j], ice[i+r][j+c], ice[i+r+c][j+c-r]
                    r += 1
                    c -= 1
                r = 0
            t += n
        p += n
        t = 0
    
    # 녹일 얼음 위치 넣을 리스트
    lst_melt = []
    
    for i in range(0,M):
        for j in range(0,M):
            cnt = 0
            for k in range(4):
                if 0 <= i+dx[k] <= M-1 and 0 <= j+dy[k] <= M-1:
                    if ice[i+dx[k]][j+dy[k]] == 0:
                        cnt += 1
                        if cnt == 2:
                            lst_melt.append((i,j))
                            break
                else:
                    cnt += 1
                    if cnt == 2:
                        lst_melt.append((i,j))
                        break

    # 리스트에 넣은 위치들의 얼음 값 -1 시켜줌
    for k in lst_melt:
        if ice[k[0]][k[1]] > 0:
            ice[k[0]][k[1]] -= 1
# 얼음 합
sum_A = 0
for i in ice:
    sum_A += sum(i)

# 가장 큰 덩어리 구하기 -> BFS
Q = deque()
cnt_ice_lst = deque()
for p in range(M):
    for q in range(M):
        if ice[p][q]:
            cnt_ice = 0
            Q.append((p,q))
            bfs()
            cnt_ice_lst.append(cnt_ice)
print(sum_A)


if cnt_ice_lst:
    print(max(cnt_ice_lst)-1)
else: # 큰 덩어리가 0이어서 cnt_ice_lst에 아무것도 안들어있을 때
    print(0)