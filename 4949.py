import sys
from collections import deque

while 1:
    la = list(map(str, sys.stdin.readline()))
    if la == ['.', '\n']:
        break
    stk = deque()
    for i in range(len(la)):
        if la[i] == '(' or la[i] == '[':
            stk.append(la[i])
        elif la[i] == ']':
            try:
                if stk[-1] == '[':
                    stk.pop()
                else: 
                    print('no')
                    break
            except:
                print('no')
                break
        elif la[i] == ')':
            try:
                if stk[-1] == '(':
                    stk.pop()
                else: 
                    print('no')
                    break
            except:
                print('no')
                break
    else:
        if stk:
            print('no')
        else:
            print('yes')