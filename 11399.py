N = int(input())
P = list(map(int, input().split()))

P.sort()
sum_1 = 0
sum_2 = 0
for i in range(N):
    sum_1 += P[i]
    sum_2 += sum_1

print(sum_2)