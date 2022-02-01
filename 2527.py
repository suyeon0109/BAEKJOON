for i in range(4):
    x,y,p,q,x2,y2,p2,q2 = map(int,input().split())

    if x>x2:
        x,x2 = x2,x
        y,y2 = y2,y
        p,p2 = p2,p
        q,q2 = q2,q
        
    if x2<p:
        if q2>y and q>y2:
            print('a')
        elif q==y2 or q2==y:
            print('b')
        else:
            print('d')
    elif x2==p:
        if q2==y or q==y2:
            print('c')
        elif q2>y and q>y2:
            print('b')
        else:
            print('d')
    else:
        print('d')
    