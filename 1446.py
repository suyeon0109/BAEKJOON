import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
N,M,K,X = map(int, input().split())

distance = [INF]*(N+1)  # start 노드에서 각 노드까지의 최단거리
graph = [[] for _ in range(N+1)]    # 각 노드에 연결되어 있는 간선

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append((b,1))

def dijkstra(start):
    q = []

    heapq.heappush(q,(0,start))

    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q) # dist : now 노드까지 갈때 거리. 최소가 아닐 수도 있음.
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1] 
            # i[1]-> now 노드에서 연결된 다른 노드까지의 거리. 여기에 dist를 더하면 start 노드에서부터의 거리가 계산됨!!
            # 즉 cost = start에서 i[0]까지의 거리

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))

town = []
flag = 0

dijkstra(X)

for j in range(1,N+1):
    if distance[j] == K:
        print(j)
        flag = 1
    
if flag == 0:
    print(-1)