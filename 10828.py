from collections import deque
import sys
stk = deque()

for _ in range(int(sys.stdin.readline())):
    la = list(map(str, sys.stdin.readline().split()))
    if la[0] == 'push':
        stk.append(la[1])
    elif la[0] == 'pop':
        try:
            print(stk.pop())
        except:
            print(-1)
    elif la[0] == 'size':
        print(len(stk))
    elif la[0] == 'empty':
        if not stk:
            print(1)
        else:
            print(0)
    else:
        try:
            print(stk[-1])
        except:
            print(-1)