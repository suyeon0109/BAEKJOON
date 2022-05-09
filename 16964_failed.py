N = int(input())
adj = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(N-1):
    a,b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

order = list(map(int, input().split()))

k = 0
visited[order[k]] = 1
t = 1


while k < N-1:
    c = 0
    if t > N-1:
        print(1)
        break
    for i in adj[order[k]]:
        if visited[i] == 0:
            c = 1
            if order[t] == i:
                k += 1
                t += 1
                visited[i] = 1
                c = 0
                break
    else:
        if c == 1:
            print(0)
            break
        else:
            k -= 1
    
    if c == 1:
        break