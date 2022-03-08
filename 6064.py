for _ in range(int(input())):
    M, N, x, y = map(int, input().split())
    a,b = 0,0
    n = 0
    while a != M or b != N:
        a += 1
        b += 1
        n += 1
        if a > M:
            a = 1
        if b > N:
            b = 1
        if a == x and b == y:
            print(n)
            break
    else:
        print(-1)
