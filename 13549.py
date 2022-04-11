from collections import deque

N, K = map(int, input().split())
visited = [-1]*100001
visited[N] = 0
Q = deque()
Q.append(N)

while Q:
    t = Q.popleft()
    if t == K:
        break

    if 0 <= 2*t <= 100000 and visited[2*t] == -1:
        visited[2*t] = visited[t]
        Q.appendleft(2*t)

    if t+1 <= 100000 and visited[t+1] == -1:
        visited[t+1] = visited[t] + 1
        Q.append(t+1)

    if 0 <= t-1 <= 100000 and visited[t-1] == -1:
        visited[t-1] = visited[t] + 1
        Q.append(t-1)


print(visited[K])