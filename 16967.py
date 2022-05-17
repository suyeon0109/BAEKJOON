H, W, X, Y = map(int, input().split())
la = [list(map(int, input().split())) for _ in range(H+X)]

for i in range(X, H+X):
    for j in range(Y, W+Y):
        la[i][j] -= la[i-X][j-Y]

for i in range(H):
    for j in range(W):
        print(la[i][j], end=' ')
    print()