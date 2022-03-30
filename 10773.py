import sys
from collections import deque

stk = deque()
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    if n == 0:
        stk.pop()
    else:
        stk.append(n)
print(sum(stk))