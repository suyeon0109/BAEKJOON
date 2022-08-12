from collections import deque
import sys

R, C = map(int, sys.stdin.readline().split())
forest = [list(map(str, sys.stdin.readline()))[:-1] for _ in range(R)]
visited = [[R*C+1]*C for _ in range(R)]

Q = deque()
P = deque()
cnt = 0
answer = R*C + 1
check = 0
S = deque()

for i in range(R):
    for j in range(C):
        if forest[i][j] == '*':
            Q.append((i,j))
        elif forest[i][j] == 'S':
            x,y = i,j
            P.append((x,y))
            visited[x][y] = 1

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs_water():

    global Q

    S = deque()

    while Q:
        a,b = Q.popleft()

        for k in range(4):
            A = a + dx[k]
            B = b + dy[k]
            if 0 <= A <= R-1 and 0 <= B <= C-1 and forest[A][B] == '.':
                forest[A][B] = '*'
                S.append((A,B))
    Q = deque(S)

def bfs_hedge():

    global answer, P

    T = deque()

    while P:
        c,d = P.popleft()

        for k in range(4):
            X = c + dx[k]
            Y = d + dy[k]
            if 0 <= X <= R-1 and 0 <= Y <= C-1:
                if forest[X][Y] == '.':
                    visited[X][Y] = visited[c][d] + 1
                    forest[X][Y] = 'S'
                    T.append((X,Y))
                elif forest[X][Y] == 'D':
                    if visited[X][Y] > visited[c][d] + 1:
                        visited[X][Y] = visited[c][d] + 1
                    answer = visited[X][Y]
                    return
        
    P = deque(T)

while P or Q:

    bfs_water()
    bfs_hedge()

if answer == R*C +1:
    print('KAKTUS')
else:
    print(answer - 1)