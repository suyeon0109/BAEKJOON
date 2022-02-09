a,b = map(int, input().split())
c,d = map(int, input().split())
e = int(input())

n = 0
def walk_x(n):
    return n + 1
def walk_y(n):
    return n + 1

for i in range(e):

    if c == a :
        def walk_x(n):
            return n - 1
        c = walk_x(c)
        n += 1
    elif c == 0 :
        def walk_x(n):
            return n + 1
        c = walk_x(c)
        n += 1
    else:
        c = walk_x(c)

    if d == b:
        def walk_y(n):
            return n - 1
        d = walk_y(d)
        n += 1
    elif d == 0:
        def walk_y(n):
            return n + 1
        d = walk_y(d)
        n += 1
    else:
        d = walk_y(d)

print(c,d)