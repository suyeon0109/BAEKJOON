N = int(input())
la = []
lb = list(map(int, input().split()))
n = 1

for i in lb:
    la.insert(len(la) - i, str(n))
    n += 1

print(' '.join(la))