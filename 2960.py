N, K = map(int, input().split())

la = [0]*(N+1)

k = 2
cnt = 0

while 1:
    for i in range(2,N+1):
        if i%k == 0 and la[i] == 0:
            la[i] += 1
            cnt += 1
            if cnt == K:
                ans = i
                break

    if cnt == K:
        break

    k += 1

print(ans)