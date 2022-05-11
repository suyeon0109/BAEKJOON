import sys

input = sys.stdin.readline

while 1:
    try:
        x = int(input())
        x *= 10**7
        n = int(input())
        la = [int(input()) for _ in range(n)]
        la.sort()

        l1, l2 = 0, 0

        start, end = 0, n-1

        while start < end:
            if la[start] + la[end] == x:
                l1, l2 = la[start], la[end]
                break
            elif la[start] + la[end] > x:
                end -= 1
            else:
                start += 1
        
        if l1 == 0 and l2 == 0:
            print('danger')
        else:
            print('yes', l1, l2)
    except:
        break