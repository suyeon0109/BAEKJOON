a,b = map(int, input().split())
c,d = map(int, input().split())
e = int(input())

if c+e < a:
    f = c + e
else:
    if (e-(a-c))//a % 2 == 0:
        f = (-1) * ((e-(a-c))%a)
    else:
        f = a + a*(-1) + (e-(a-c))%a

if (e-(b-d))//b % 2 == 0:
    g = (-1) * ((e-(b-d))%b)
else:
    g = b + b*(-1) + (e-(b-d))%b

print(f,g)
