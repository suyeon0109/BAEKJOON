from collections import deque

N, M = map(int, input().split())

dud = deque()
bo = deque()

for _ in range(N):
    dud.append(input())
for _ in range(M):
    bo.append(input())

jab = list(set(dud) & set(bo))
jab.sort()
print(len(jab))
for i in jab:
    print(i)