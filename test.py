H, W, X, Y = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(H + X)]

for i in range(X, H+X):
    for j in range(Y, W+Y):
        