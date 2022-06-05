from collections import deque

N, K = map(int, input().split())
durab = list(map(int, input().split()))
durab = deque(durab)
robot = deque([0]*2*N)
cnt = 0

while 1:
    cnt += 1
    
    # 1.
    durab.rotate(1)
    robot.rotate(1)
    if robot[N-1] == 1:
        robot[N-1] = 0

    # 2.
    for i in range(N,-1,-1):
        if robot[i] == 1 and robot[i+1] == 0 and durab[i+1] > 0:
            robot[i] = 0
            robot[i+1] = 1
            durab[i+1] -= 1
            if robot[N-1] == 1:
                robot[N-1] = 0

    # 3.
    if durab[0] > 0:
        robot[0] = 1
        durab[0] -= 1

    # 4.
    if durab.count(0) >= K:
        break

print(cnt)