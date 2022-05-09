N, L = map(int, input().split())
pipe = [0]*1001

la = list(map(int, input().split()))
for i in la:
    pipe[i] = 1

cnt = 0
for j in range(1001):
    if pipe[j] == 1:
        cnt += 1
        for k in range(L):
            if j+k <= 1000:
                pipe[j+k] = 0

print(cnt)
