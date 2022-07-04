import sys

N = int(input())
la = []

for _ in range(N):
    a,b = map(int, sys.stdin.readline().split())
    la.append([a,b,0])

t = la.pop(0)
p, q = t[0],t[1]

# t       = [a,b,0]
# la[i]   = [c,d,0] -> [c-a, d-b, 0]
# la[i+1] = [e,f,0] -> [e-a, f-b, 0]

ssum = 0
for i in range(len(la)-1):
    a = (la[i][0] - p) * (la[i+1][1] - q) - (la[i][1] - q) * (la[i+1][0] - p)
    s = a / 2
    ssum += s

print(abs(ssum))