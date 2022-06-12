from collections import deque
import math
import sys

N = int(sys.stdin.readline())
la = deque()

def prime(N):
    for i in range(3, N+1, 2):
        for j in range(2, int(math.sqrt(i))+1):
            if i%j == 0:
                break
        else:
            la.append(i)

la.appendleft(2)
prime(N)

def ans(la):
    cnt = 0
    plus = 0

    k = 0
    m = 0
    while 1:
        if plus < N:
            if k > len(la)-1:
                return cnt
            plus += la[k]
            k += 1
        elif plus == N:
            cnt += 1
            plus -= la[m]
            m += 1
        elif plus > N:
            plus -= la[m]
            m += 1

print(ans(la))