from collections import deque
import sys

N,M = map(int, sys.stdin.readline().split())
castle = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
visited = [[0]*N for _ in range(M)]
Q = deque()
dx = [0,-1,0,1]
dy = [-1,0,1,0]
room_cnt = 0
room_max = 0
room_sum = 0
rooms = deque()
rooms.append(0)
num = 1

def bfs():

    global room_max, num, rooms, adj, room_sum
    room = 1

    adj = deque()

    while Q:
        a,b = Q.popleft()
        dir = format(castle[a][b],'b').zfill(4)[::-1]
        for i in range(len(dir)):
            if 0 <= a+dx[i] <= M-1 and 0 <= b+dy[i] <= N-1:
                if dir[i] == '0' and visited[a+dx[i]][b+dy[i]] == 0:
                    Q.append((a + dx[i], b + dy[i]))
                    room += 1
                    visited[a + dx[i]][b + dy[i]] = num
                elif dir[i] == '1' and visited[a+dx[i]][b+dy[i]] != num:
                    adj.append(visited[a+dx[i]][b+dy[i]])
    
    for i in adj:
        summ = room + rooms[i]
        if summ > room_sum:
            room_sum = summ
    rooms.append(room)

    if room_max < room:
        room_max = room

for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            room_cnt += 1
            Q.append((i,j))
            visited[i][j] = num
            bfs()
            num += 1

print(room_cnt)
print(room_max)
print(room_sum)
