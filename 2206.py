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