n = int(input())
for i in range(n):
    lA = list(map(int, input().split()))
    lB = list(map(int, input().split()))

    lA = [lA[1:].count(4), lA[1:].count(3), lA[1:].count(2), lA[1:].count(1)]
    lB = [lB[1:].count(4), lB[1:].count(3), lB[1:].count(2), lB[1:].count(1)]

    for i in range(4):
        if lA[i]>lB[i]:
            print('A')
            break
        elif lB[i]>lA[i]:
            print('B')
            break

    if lA == lB:
        print('D')