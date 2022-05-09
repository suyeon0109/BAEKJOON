N, S, P = map(int, input().split())

if N != 0:
    lst = list(map(int, input().split()))
    if N == P and min(lst) >= S:
        print(-1)
    else:
        lst.append(S)
        lst.sort(reverse=True)

        print(lst.index(S) + 1)

else:
    print(1)