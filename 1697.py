from collections import deque

N, K = map(int, input().split())
Q = deque()
Q.append(N)
visited = [0]*1000001
visited[N] = 1
def time():
    while Q:
        if N == K:
            return 0
        t = Q.popleft()
        p = visited[t]
        for i in [t+1, t-1, 2*t]:
            if 0<=i<=100000:
                if visited[i] == 0:
                    Q.append(i)
                    visited[i] = p+1
                if i == K:
                    return p
print(time())