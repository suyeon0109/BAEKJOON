N = int(input())
A = list(map(int, input()))
B = list(map(int, input()))
C = A[:]

cnt = 0
cnt_2 = 0

for i in range(1,N):

    if i == N-1:
        if A[i-1] != B[i-1]:
            cnt += 1
            for k in range(2):
                if A[i-1+k] == 0:
                    A[i-1+k] = 1
                else:
                    A[i-1+k] = 0        
    else:
        if A[i-1] != B[i-1]:
            cnt += 1
            for k in range(3):
                if A[i-1+k] == 0:
                    A[i-1+k] = 1
                else:
                    A[i-1+k] = 0


cnt_2 += 1
for q in range(2):
    if C[q] == 0:
        C[q] = 1
    else:
        C[q] = 0


for i in range(1,N):

    if i == N-1:
        if C[i-1] != B[i-1]:
            cnt_2 += 1
            for k in range(2):
                if C[i-1+k] == 0:
                    C[i-1+k] = 1
                else:
                    C[i-1+k] = 0        
    else:
        if C[i-1] != B[i-1]:
            cnt_2 += 1
            for k in range(3):
                if C[i-1+k] == 0:
                    C[i-1+k] = 1
                else:
                    C[i-1+k] = 0
   

if A[-1] == B[-1]:
    print(cnt)
elif C[-1] == B[-1]:
    print(cnt_2)
else:
    print(-1)