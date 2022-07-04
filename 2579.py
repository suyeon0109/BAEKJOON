from collections import deque
import sys

N = int(sys.stdin.readline())
la = deque()

for _ in range(N):
    la.append(int(sys.stdin.readline()))
lb = deque()

def stairs(n):
    if n == 0:
        lb.append(la[0])
    elif n == 1:
        lb.append(la[0]+la[1])
    elif n == 2:
        lb.append(max(la[0]+la[2], la[1]+la[2]))
    else:
        lb.append(max(lb[n-3]+la[n-1]+la[n], lb[n-2]+la[n]))


for i in range(N):
    stairs(i)

print(lb[-1])