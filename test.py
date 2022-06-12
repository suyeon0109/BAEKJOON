import sys

N, M = map(int, sys.stdin.readline().split())

bus = [[10000]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    bus[a][b] = c

one = bus[0]

def dijkstra():

    while 1:
        min()

print(bus)