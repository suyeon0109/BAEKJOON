N,K = map(int, input().split())
seq = list(map(int, input().split()))
sum_n = sum(seq[:K])
max_n = sum(seq[:K])
for i in range(len(seq)-K):
    if sum_n+seq[K+i]-seq[i] > max_n:
        max_n = sum_n+seq[K+i]-seq[i]
    sum_n = sum_n+seq[K+i]-seq[i]
    
print(max_n)


