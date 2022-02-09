a,b = map(int, input().split())
c,d = map(int, input().split())
e = int(input())

if c+e < a:
    f = c + e
else:
    if (e-(a-c))//a % 2 == 0:
        f = a - (e-a+c)%a
    else:
        f = (e-a+c)%a

if d+e < b:
    g = d + e
else:
    if (e-(b-d))//b % 2 == 0:
        g = b - (e-b+d)%b
    else:
        g = (e-b+d)%b

print(f,g)
