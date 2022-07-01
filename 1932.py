import sys
import copy

N = int(input())

la = [[0,0]] + [[0] + list(map(int, sys.stdin.readline().split())) + [0] for _ in range(N)]
calc = copy.deepcopy(la)
ssum = 0

for p in range(1,N+1):
    for q in range(1,p+1):
        ssum = max(calc[p-1][q-1:q+1])
        calc[p][q] = ssum + la[p][q]

print(max(calc[N]))