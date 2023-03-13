from collections import deque
import sys

N = int(sys.stdin.readline())

island = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

Q = deque()
R = deque()

def bfs_land():
    while Q:
        a,b = Q.popleft()
        for k in range(4):
            A = a + dx[k]
            B = b + dy[k]
            if 0 <= A <= N-1 and 0 <= B <= N-1 and island[A][B] and visited_land[A][B] == 0:
                Q.append((A,B))
                visited_land[A][B] = visited_land[a][b]

def bfs_dist():
    global min_dist, land
    while R:
        a,b = R.popleft()
        for k in range(4):
            A = a + dx[k]
            B = b + dy[k]
            if 0 <= A <= N-1 and 0 <= B <= N-1 and not island[A][B] and visited_dist[A][B] == 0:
                R.append((A,B))
                visited_dist[A][B] = visited_dist[a][b] + 1

            elif 0 <= A <= N-1 and 0 <= B <= N-1 and island[A][B] and visited_land[A][B] != land:
                if visited_dist[a][b] < min_dist:
                    min_dist = visited_dist[a][b]

visited_land = [[0]*N for _ in range(N)]
chk = 1
min_dist = N**2

for i in range(N):
    for j in range(N):
        if island[i][j] and not visited_land[i][j]:
            visited_land[i][j] = chk
            chk += 1
            Q.append((i,j))
            bfs_land()

for p in range(N):
    for q in range(N):
        if island[p][q]:
            visited_dist = [[0]*N for _ in range(N)]
            visited_dist[p][q] = 1
            land = visited_land[p][q]
            R.append((p,q))
            bfs_dist()

print(min_dist-1)