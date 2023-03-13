import sys
N = int(input())
la = []

for _ in range(N):
    la.append(int(sys.stdin.readline()))

la.sort()

weight = la[0] * N
n = 1
while n <= (N-1):
    if weight < la[n] * (N-n):
        weight = la[n] * (N-n)
    n += 1

print(weight)