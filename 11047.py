import sys

N, K = map(int, input().split())
la = [int(sys.stdin.readline()) for _ in range(N)]
cnt = 0

for i in range(len(la)-1,-1,-1):
    if la[i] <= K:
        cnt += K//la[i]
        K -= (K//la[i])*la[i]

print(cnt)