import sys

n = int(input())
for _ in range(n):
    N, M = map(int,sys.stdin.readline().split())
    m = 1
    n = 1
    cnt = 1

    if N != M:
        while cnt <= N:
            m *= M
            M -= 1
            cnt += 1
        
        while N > 1:
            n *= N
            N -= 1
    
    print(m//n)