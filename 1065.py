N = int(input())

def ans(N):
    if N < 100:
        return N
    elif 100 <= N <= 110:
        return 99
    else:
        cnt = 0
        if N == 1000:
            N = 999
        for i in range(111, N+1):
            num = str(i)
            if int(num[0]) - int(num[1]) == int(num[1]) - int(num[2]):
                cnt += 1
        
        return cnt + 99

print(ans(N))