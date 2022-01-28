list_area = []
for i in range(4):
    x1,y1,x2,y2 = map(int, input().split())

    if x2>x1:
        x1,x2 = x2,x1
    if y2>y1:
        y1,y2 = y2,y1

    for i in range(1, x1-x2+1):
        for j in range(1, y1-y2+1):
            list_area.append((x1-i,y1-j))

print(len(set(list_area)))
