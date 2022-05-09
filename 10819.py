from itertools import permutations

N = int(input())

A = list(map(int, input().split()))

order_lst = list(permutations(A, N))
sum_max = 0


for order in order_lst:
    sum = 0
    for i in range(N-1):
        sum += abs(order[i] - order[i+1])
    
    if sum > sum_max:
        sum_max = sum

print(sum_max)