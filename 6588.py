import math
import sys

def ans(N):
    for i in range(3, N//2+1, 2):
        for j in range(2, int(math.sqrt(i))+1):
            if i%j == 0:
                break
        else:
            k = N-i
            for j in range(2, int(math.sqrt(k))+1):
                if k%j == 0:
                    break
            else:
                print(f'{N} = {i} + {k}')
                return
    else:
        return 'Goldbach\'s conjecture is wrong.'

while 1:
    try:
        N = int(sys.stdin.readline())
        ans(N)
    except:
        break