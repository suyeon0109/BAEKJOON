N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort(reverse=True)
B.sort()
C = 0
for i in range(N):
    C += A[i]*B[i]

print(C)