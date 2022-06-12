N = int(input())

la = list(map(int, input().split()))

m = max(la)

for i in range(len(la)):
    la[i] = la[i]/m*100

print(sum(la)/len(la))
