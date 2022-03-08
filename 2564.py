A,B = map(int,input().split())
n = int(input())
la = [list(map(int,input().split())) for _ in range(n+1)]
lb = [[0,0] for _ in range(n+1)]
k = 0

for j in la:
    if j[0]==1:
        x,y = j[1], B

    elif j[0]==2:
        x,y = j[1], 0
        j[0] = 3

    elif j[0]==3:
        x,y = 0, B-j[1]
        j[0] = 4

    else:
        x,y = A, B-j[1]
        j[0] = 2

    lb[k][0] = x
    lb[k][1] = y
    k += 1

s = 0
for i in range(len(la)-1):
    if abs(la[i][0] - la[-1][0]) == 2:
        q = lb[i][0]+lb[-1][0] + abs(lb[i][1]-lb[-1][1])
        if q > A+B:
            s += 2*(A+B) - q
        else:
            s += q
    else:
        s += abs(lb[i][0] - lb[-1][0]) + abs(lb[i][1]-lb[-1][1])

print(s)