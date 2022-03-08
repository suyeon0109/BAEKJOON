n = int(input())
la = list(map(int, input().split()))
up = 1
down = 1
lb = []

if n == 1:
    lb.append(up)
for i in range(n-1):
    if la[i] < la[i+1]:
        # lb.append(down)
        up += 1
        down = 1
        lb.append(up)
    elif la[i] > la[i+1]:
        # lb.append(up)
        up = 1
        down += 1
        lb.append(down)
    else:
        up += 1
        down += 1
        lb.append(up)
        lb.append(down)
print(max(lb))

