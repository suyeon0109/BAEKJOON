from collections import deque
import sys

dx = [0,1,0,-1]
dy = [1,0,-1,0]

puyo = [list(map(str, sys.stdin.readline()))[:-1] for _ in range(12)]
puyo_rot = [[] for _ in range(6)]
puyo_rot_n = puyo_rot

def rot(lst):
    global puyo, puyo_rot
    for j in range(6):
        for i in range(11,-1,-1):
            puyo_rot[j].append(puyo[i][j])
    
    return puyo_rot

rot(puyo)

Q = deque()
R = deque()
S = deque()

cnt_kill = 0

def bfs():

    global R, cnt_kill, cnt, puyo_rot, flag, visited

    while Q:
        a,b = Q.popleft()
        visited[a][b] = 1

        for k in range(4):
            A = a+dx[k]
            B = b+dy[k]
            if 0 <= A <= 5 and 0 <= B < len(puyo_rot[A]) and puyo_rot[A][B] == puyo_rot[a][b] and visited[A][B] == 0:
                Q.append((A,B))
                R.append([A,B])
                visited[A][B] = 1
                cnt += 1

    if cnt >= 4:
        S.extend(R)
        flag = 1
    
    cnt = 1


cnt = 1
while 1:

    S = deque()

    flag = 0
    cnt = 1
    visited = [[0]*12 for _ in range(6)]

    for i in range(6):
        for j in range(12):
            
            R = deque()

            if 0 <= j < len(puyo_rot[i]) and puyo_rot[i][j] != '.' and visited[i][j] == 0:

                Q.append((i,j))
                R.append([i,j])
                bfs()
                
    if flag == 1:
        puyo_rot_n = [[] for _ in range(6)]

        for i in range(6):
            for j in range(len(puyo_rot[i])):
                if [i,j] in S:
                    pass
                else:
                    puyo_rot_n[i].append(puyo_rot[i][j])

    puyo_rot = puyo_rot_n

    if flag :
        cnt_kill += 1
    elif flag == 0:
        break
    
print(cnt_kill)