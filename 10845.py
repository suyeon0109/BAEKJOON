from collections import deque
import sys

N = int(input())
Q = deque()

def queue(lst):
    if lst[0] == 'push':
        Q.append(int(lst[1]))

    elif lst[0] == 'pop':
        if Q:
            print(Q.popleft())
        else:
            print(-1)

    elif lst[0] == 'size':
        print(len(Q))

    elif lst[0] == 'empty':
        if Q:
            print(0)
        else:
            print(1)

    elif lst[0] == 'front':
        if Q:
            print(Q[0])
        else:
            print(-1)
            
    else:
        if Q:
            print(Q[-1])
        else:
            print(-1)

for _ in range(N):
    order = list(map(str, sys.stdin.readline().split()))
    queue(order)