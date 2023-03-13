import sys

board = []
visited = [[0]*5 for _ in range(5)]

for _ in range(5):
    lb = list(map(int, sys.stdin.readline().split()))
    board.append(lb)

r,c = map(int, sys.stdin.readline().split())
visited[r][c] = 1

dx = [0,1,0,-1]
dy = [1,0,-1,0]
apple = 0
cnt = 0
answer = 0

def dfs(a,b):
    global apple, answer, cnt
    if board[a][b] == 1:
        apple += 1
    
    if apple >= 2:
        answer = 1

    if answer == 1 or cnt == 3:
        return

    for k in range(4):
        X = a + dx[k]
        Y = b + dy[k]
        if 0 <= X < 5 and 0 <= Y < 5 and board[X][Y] != -1 and visited[X][Y] == 0:
            cnt += 1

            visited[X][Y] = 1

            # for i in range(5):
            #     print(visited[i])
            # print('cnt: ', cnt)
            # print('apple: ', apple)
            # print()

            dfs(X, Y)
            if board[X][Y] == 1:
                apple -= 1
            visited[X][Y] = 0
            cnt -= 1

dfs(r,c)

print(answer)