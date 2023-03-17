import sys
from collections import deque
N = int(input())

height = []
loc = deque()
area_max = 1
rain = 1

flag = 0

for _ in range(N):
    la = list(map(int, sys.stdin.readline().split()))
    height.append(la)

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs():
    while loc:
        a,b = loc.popleft()
        for k in range(4):
            X = a + dx[k]
            Y = b + dy[k]
            if 0 <= X <= N-1 and 0 <= Y <= N-1 and visited[X][Y] == 0 and height[X][Y] > rain:
                loc.append((X,Y))
                visited[X][Y] = 1


while rain <= 100:
    visited = [[0]*N for _ in range(N)]
    area = 0
    for i in range(N):
        for j in range(N):
            if height[i][j] > rain and visited[i][j] == 0:
                visited[i][j] = 1
                loc.append((i,j))
                area += 1
                bfs()

    if area_max < area:
        area_max = area
    
    if area_max != 1 and area == 1 and flag == 1:
        break

    flag = 1
    rain += 1

print(area_max)