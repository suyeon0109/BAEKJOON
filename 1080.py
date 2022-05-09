N, M = map(int, input().split())
A = [list(map(int, input())) for _ in range(N)]
B = [list(map(int, input())) for _ in range(N)]

cnt = 0
def ans():
    global cnt

    for i in range(N):
        for j in range(M):
            if A[i][j] != B[i][j]:
                if N-1 - i < 2 or M-1 - j < 2:
                    cnt = -1
                    return 
                else:
                    for p in range(i,i+3):
                        for q in range(j, j+3):
                            if A[p][q] == 1:
                                A[p][q] = 0
                            else:
                                A[p][q] = 1
                    cnt += 1
ans()
print(cnt)