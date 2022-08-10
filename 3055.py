from collections import deque
import sys

R, C = map(int, sys.stdin.readline().split())
forest = [list(map(str, sys.stdin.readline()))[:-1] for _ in range(R)]
visited = [[0]*C for _ in range(R)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
Q = deque()
cnt = 0
flag = 0
answer = 0
check = 0
S = deque()

for i in range(R):
    for j in range(C):
        if forest[i][j] == '*':
            Q.append((i,j))
        elif forest[i][j] == 'S':
            x,y = i,j

def bfs():
    global flag, Q, check

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
    check = 0

def dfs(p,q):
    
    global cnt, flag, answer, check

    if check :
        bfs()

    if flag:
        return

    if p<0 or p > R-1 or q<0 or q > C-1:
        return


    if forest[p][q] == 'S':

        check = 0
        return

    if forest[p][q] == '.':

        forest[p][q] = 'S'

        visited[p][q] = 1
        cnt += 1
        check = 1

        dfs(p+1,q)
        dfs(p-1,q)
        dfs(p,q+1)
        dfs(p,q-1)
        for a,b in S:
            forest[a][b] = '.'

    elif forest[p][q] == 'D':
        cnt += 1
        answer = cnt
        cnt = 0
        flag = 1
        return

    else:
        check = 0
        return

check = 1
dfs(x+1,y)
dfs(x-1,y)
dfs(x,y+1)
dfs(x,y-1)

if flag :
    print(answer-1)
else:
    print('KAKTUS')