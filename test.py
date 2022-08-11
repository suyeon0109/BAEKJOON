from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())

mapp = [list(map(str, sys.stdin.readline()))[:-1] for _ in range(N)]
visited_0 = [[N*M+1]*M for _ in range(N)]
visited_1 = [[N*M+1]*M for _ in range(N)]
ans0 = N*M+1
ans1 = N*M+1

dx = [0,1,0,-1]
dy = [1,0,-1,0]

Q = deque()
Q.append([0,0,0])
visited_0[0][0] = 1

def bfs():

    global ans0, ans1

    while Q:
        t = Q.popleft()
        a,b,c = t[0], t[1], t[2]
        for k in range(4):
            A = a+dx[k]
            B = b+dy[k]
            if A == N-1 and B == M-1:
                if c == 0:
                    if ans0 > visited_0[a][b] + 1:
                        ans0 = visited_0[a][b] + 1
                else:
                    if ans1 > visited_1[a][b] + 1:
                        ans1 = visited_1[a][b] + 1
                return
            elif 0<=A<=N-1 and 0<=B<=M-1:
                if mapp[A][B] == '0':
                    if c == 0:
                        if visited_0[A][B] > visited_0[a][b] + 1:
                            Q.append([A,B,c])
                            visited_0[A][B] = visited_0[a][b] + 1
                    else:
                        if visited_1[A][B] > visited_1[a][b] + 1:
                            Q.append([A,B,c])
                            visited_1[A][B] = visited_1[a][b] + 1
                        
                else:
                    if not c:
                        if visited_1[A][B] > visited_0[a][b] + 1:
                            Q.append([A,B,1])
                            visited_1[A][B] = visited_0[a][b] + 1
            
bfs()

if N == M == 1:
    print(1)
elif ans0 == N*M+1 and ans1 == N*M+1:
    print(-1)
else:
    print(min(ans0,ans1))





# def dfs(a,b):

#     global crush, cnt, ans, depart

#     if cnt >= ans:
#         return

#     if a<0 or b<0 or a>=N or b>=M:
#         return

#     if a == N-1 and b == M-1:
#         depart = 1
#         if ans > cnt:
#             ans = cnt
#         return 

#     if mapp[a][b] == '1':
#         if crush:
#             return 
#         else:
#             crush = 1
#             cnt += 1
#             mapp[a][b] = '0'
#             visited[a][b] = 1
#             dfs(a+1,b)
#             dfs(a-1,b)
#             dfs(a,b+1)
#             dfs(a,b-1)
#             visited[a][b] = 0
#             crush = 0
#             cnt -= 1

#     elif mapp[a][b] == '0' and visited[a][b] == 0:
#         visited[a][b] = 1
#         cnt += 1
#         dfs(a-1,b)
#         dfs(a+1,b)
#         dfs(a,b-1)
#         dfs(a,b+1)
#         visited[a][b] = 0
#         cnt -= 1

# dfs(0,0)
# if depart :
#     print(ans)
# else:
#     print(-1)