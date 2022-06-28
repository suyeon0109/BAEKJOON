A, B, C = map(int, input().split())
cnt = 1

if B>=C:
    print(-1)

else:

    D = C-B
    print(A//D + 1)