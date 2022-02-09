import math

N, K = map(int, input().split())
d1 = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}

for i in range(N):
    a,b = map(int, input().split())
    d1[b].append(a)

cnt = 0
for i in range(1,7):
    for j in range(2):
        cnt += math.ceil(d1[i].count(j)/K)

print(cnt)