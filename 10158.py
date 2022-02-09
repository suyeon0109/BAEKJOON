a,b = map(int, input().split())
c,d = map(int, input().split())
e = int(input())

cnt_x = c
cnt_y = d

m = 0
n = 0
for i in range(e):

    if a * m <= cnt_x < a * (m+1):
        c += (-1)**(m)
        cnt_x += 1
    else:
        c += (-1)**(m+1)
        m += 1
        cnt_x += 1
    
    if b * n <= cnt_y < b * (n+1):
        d += (-1)**(n)
        cnt_y += 1
    else:
        d += (-1)**(n+1)
        n += 1
        cnt_y += 1

print(c,d)