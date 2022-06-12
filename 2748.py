from collections import deque

fibo = [0,1]
fibo = deque(fibo)

def fibonacci(n):
    if n == 0 or n == 1:
        return fibo[n]
    else:
        for i in range(2,n+1):
            fibo.append(fibo[i-1]+fibo[i-2])
        return fibo[n]

print(fibonacci(int(input())))