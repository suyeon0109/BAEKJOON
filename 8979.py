N, K = map(int, input().split())
medal = []
for _ in range(N):
    a, b, c, d = map(int, input().split())
    medal.append((b,c,d))
    if a == K:
        (x,y,z) = (b,c,d)

medal.sort(reverse=True)
print(medal.index((x,y,z))+1)