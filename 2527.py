for i in range(4):
    area = []
    area2 = []
    dot = []
    dot2 = []

    x,y,p,q,x2,y2,p2,q2 = map(int, input().split())

    for i in range(0, p-x):
        for j in range(0, q-y):
            area.append((p-i,q-j))
    for i in [x,p]:
        for j in range(y,q+1):
            dot.append((i,j))
    for i in [y,q]:
        for j in range(x,p+1):
            dot.append((j,i))

    for i in range(0, p2-x2):
        for j in range(0, q2-y2):
            area2.append((p2-i,q2-j))
    for i in [x2,p2]:
        for j in range(y2,q2+1):
            dot2.append((i,j))
    for i in [y2,q2]:
        for j in range(x2,p2+1):
            dot2.append((j,i))


    a = len(set(area))
    b = len(set(area)-set(area2))
    c = len(set(dot))
    d = len(set(dot)-set(dot2))

    if a != b:
        print('a')
    elif c != d:
        if c == (d + 1):
            print('c')
        else:
            print('b')
    else:
        print('d')

