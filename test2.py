N = int(input())

def ans(N):
    if N < 100:
        return N
    elif 100 <= N <= 110:
        return 99
    else:
        start = 111
        
        for i in range(111, N):
