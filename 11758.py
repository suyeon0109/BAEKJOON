x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())


def CCW():
    if x1 == x2:
        if x2 == x3:
            print(0)
        elif x2 < x3:
            if y2 > y1:
                print(-1)
            else:
                print(1)
        else:
            if y2 > y1:
                print(1)
            else:
                print(-1)

    elif x1 == x3:
        if x3 < x2:
            if y3 > y1:
                print(1)
            else:
                print(-1)
        else:
            if y3 > y1:
                print(-1)
            else:
                print(1)
    elif x2 == x3:
        if x3 > x1:
            if y3 > y2:
                print(1)
            else:
                print(-1)
        else:
            if y3 > y2:
                print(-1)
            else:
                print(1)
    else:
        if (y2-y1) * (x3-x1) < (y3-y1) * (x2-x1):
            print(1)
        elif (y2-y1) * (x3-x1) > (y3-y1) * (x2-x1):
            print(-1)
        else:
            print(0)

CCW()