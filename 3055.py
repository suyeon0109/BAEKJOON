from collections import deque
import sys

R, C = map(int, sys.stdin.readline().split())
forest = [list(map(str, sys.stdin.readline()))[:-1] for _ in range(R)]
visited = [[0]*C for _ in range(R)]

Q = deque()
cnt = 0
answer = R*C
check = 0
S = deque()

for i in range(R):
    for j in range(C):
        if forest[i][j] == '*':
            Q.append((i,j))
        elif forest[i][j] == 'S':
            x,y = i,j
            visited[x][y] = 1
        elif forest[i][j] == 'D':
            w,z = i,j

if x <= w:
    if y <= z:
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
    else:
        dx = [1,0,-1,0]
        dy = [0,-1,0,1]
else:
    if y <= z:
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
    else:
        dx = [-1,0,1,0]
        dy = [0,-1,0,1]


def bfs():
    global Q, check

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
    global cnt, answer, check

    if cnt > answer:
        return 

    if p<0 or p > R-1 or q<0 or q > C-1:
        return

    if check :
        bfs()

    elif forest[p][q] == '.':

        forest[p][q] = 'S'
        visited[p][q] = 1

        for k in range(4):
            if 0 <= p+dx[k] <= R-1 and 0 <= q+dy[k] <= C-1 and forest[p+dx[k]][q+dy[k]] == 'D':
                cnt += 1
                if answer > cnt +1:
                    answer = cnt +1
                forest[p][q] = '.'
                visited[p][q] = 0
                cnt -= 1
                return

        cnt += 1
        check = 1

        dfs(p-1,q)
        dfs(p+1,q)
        dfs(p,q-1)
        dfs(p,q+1)
        forest[p][q] = '.'
        visited[p][q] = 0
        cnt -= 1

        for a,b in S:
            forest[a][b] = '.'
        

    elif forest[p][q] == 'D':
        cnt += 1
        if answer > cnt:
            answer = cnt
        cnt -= 1

        return

    else:
        check = 0
        return

check = 1
for k in range(4):
    if 0 <= x+dx[k] <= R-1 and 0 <= y+dy[k] <= C-1 and forest[x+dx[k]][y+dy[k]] == 'D':
        answer = 1
        break
else:        
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y+1)
    dfs(x,y-1)

if answer != R*C :
    print(answer)
else:
    print('KAKTUS')