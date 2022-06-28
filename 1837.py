from collections import deque
import math
import sys
P, K = map(int, sys.stdin.readline().split())
la = deque()

def prime(N):
    for i in range(3, N, 2):
        for j in range(2, int(math.sqrt(i))+1):
            if i%j == 0:
                break
        else:
            la.append(i)
if K != 2:
    la.appendleft(2)
prime(K)

for i in la:
    if P%i == 0:
        print('BAD', i)
        break
else:
    print('GOOD')