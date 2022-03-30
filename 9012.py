import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    m = sys.stdin.readline()
    stk = deque()
    for i in range(len(m)-1):
        if m[i] == '(':
            stk.append(m[i])
        else:
            try:
                stk.pop()
            except:
                print('NO')
                break
    else:
        if len(stk) != 0:
            print('NO')
        else:
            print('YES')