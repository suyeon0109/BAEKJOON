N, M = map(int, input().split())
la = list(map(int, input().split()))

cnt = 0

for i in range(N):
    s = 0
    for j in range(i,N):
        s += la[j]
        if s == M:
            cnt += 1

print(cnt)