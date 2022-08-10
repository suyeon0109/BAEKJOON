import sys
sys.setrecursionlimit(10**6)

def dfs(n):
    global la, lb, visited, cnt

    if visited[n]:
        cnt += 1
        return
    
    visited[n] = 1

    dfs(lb[n][0])


for _ in range(int(sys.stdin.readline())):

    N = int(sys.stdin.readline())

    la = [0] + list(map(int, sys.stdin.readline().split()))
    lb = [[] for _ in range(N+1)]
    visited = [0]*(N+1)

    for i in range(1,N+1):
        lb[i].append(la[i])
    
    cnt = 0

    for j in range(1,N+1):
        if not visited[j]:
            dfs(j)
    
    print(cnt)