import sys
dx = [0,0,-1,-1,-1,0,1,1,1]
dy = [0,-1,-1,0,1,1,1,0,-1]

N, M = map(int, input().split())
cloud = [[N-1,0], [N-1,1], [N-2,0], [N-2,1]]
grnd = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for _ in range(M):
    excpt = [[0]*N for _ in range(N)] 
    d,s = map(int, sys.stdin.readline().split())

    for p in cloud:
        p[0] = (p[0] + dx[d]*s) % N
        p[1] = (p[1] + dy[d]*s) % N

    for p in cloud:
        grnd[p[0]][p[1]] += 1
        excpt[p[0]][p[1]] = 1
    
    for p in cloud:
        for i in range(2,9,2):
            if 0 <= p[0] + dx[i] <= N-1 and 0 <= p[1] + dy[i] <= N-1:
                if grnd[p[0] + dx[i]][p[1] + dy[i]] > 0:
                    grnd[p[0]][p[1]] += 1

    cloud = []
    for j in range(N):
        for k in range(N):
            if grnd[j][k] > 1 and excpt[j][k] == 0:
                grnd[j][k] -= 2
                cloud.append([j,k])

water = 0
for i in grnd:
    water += sum(i)
print(water)