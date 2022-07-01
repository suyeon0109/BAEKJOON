import sys

N, M = map(int, input().split())

la = list(map(int, sys.stdin.readline().split()))

lb = [0]*N
ssum = 0
for i in range(N):
    ssum += la[i]
    lb[i] = ssum

for _ in range(M):
    i,j = map(int, sys.stdin.readline().split())
    if i != 1:
        print(lb[j-1] - lb[i-2])
    else:
        print(lb[j-1])