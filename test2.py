N = int(input())
num = [0]*1000001
if N == 1 or N == 2:
    print(2)
elif N == 3:
    print(3)
else:
    for i in range(2,N):
        k = 1
        while i*k <= 1000000:
            num[i*k] = -1
            k += 1

    for j in range(N, 1000001):
        if num[j] != -1 and str(j) == str(j)[::-1]:
            print(j)
            break
        else:
            k = 1
            while i*k <= 1000000:
                num[i*k] = -1
                k += 1

