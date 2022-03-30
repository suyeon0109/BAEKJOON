from itertools import combinations
from copy import deepcopy

front = rear = 0
def enq(a,b):
    global rear 
    rear = (rear+1)%len(Q)
    Q[rear] = (a,b)
def deq():
    global front
    if isEmp():
        return 'Q is empty'
    else:
        front = (front+1)%len(Q)
        return Q[front]

def isEmp():
    return front == rear

def maze():
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    sum = 0
    while not isEmp():
        p = deq()
        I,J = p[0],p[1]

        for k in range(4):
            if 0 <= I+dx[k] <= N-1 and 0 <= J+dy[k] <= M-1:
                if lc[I+dx[k]][J+dy[k]] == 0:
                    enq(I+dx[k],J+dy[k])
                    lc[I+dx[k]][J+dy[k]] = 1

    for i in range(N):
        sum += lc[i].count(0)
    return sum


N,M = map(int, input().split())
la = [list(map(int, input().split())) for _ in range(N)]
Q = [(0,0)]*M*N
space = []
sum_max = 0

for i in range(N):
    for j in range(M):
        if la[i][j] == 2:
            enq(i,j)

for s in range(N):
    for j in range(M):
        if la[s][j] == 0:
            space.append((s,j))

lb = list(combinations(space, 3))

for i in lb:
    lc = deepcopy(la)
    for j in i:
        lc[j[0]][j[1]] = 1

    result = maze()
    if sum_max < result:
        sum_max = result


print(sum_max)