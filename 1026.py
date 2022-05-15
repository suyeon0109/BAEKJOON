N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 값이 최소가 되려면, 큰수는 작은수랑, 작은수는 큰수랑 곱하면 된다.
# -> 서로 반대로 정렬해서 곱해주면 된다.
A.sort(reverse=True)
B.sort()

C = 0
for i in range(N):
    C += A[i]*B[i]

print(C)