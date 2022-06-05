N, M = map(int, input().split())
la = list(map(int, input().split()))
la.sort()

if N == 1:
    height = la[0] - M

s = 0
for i in range(N-1, 0, -1):
    s += (la[i]-la[i-1]) * (N - i)

    if s >= M:
        height = la[i-1]
        tree = i
        break

if s > M:
    while s > M:
        s -= N - tree
        height += 1
        if s < M:
            s += N - tree
            height -= 1
            break
elif s < M:
    height = la[0]
    while s < M:
        s += N
        height -= 1


print(height)