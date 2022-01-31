n = int(input())
way = {1:[], 2:[], 3:[], 4:[]}
order = []
cnt = 0

for i in range(6):
    a,b = map(int, input().split())
    order.append(a)
    way[a].append(b)

if len(way[1]) == 2:
    if len(way[3])==2:
        if order[:2]==[1,3]:
            area = way[2][0]*way[4][0] - way[1][0]*way[3][0]
        elif order[:3] == [3,1,4]:
            area = way[2][0]*way[4][0] - way[1][1]*way[3][0]
        elif order[:2]==[1,4]:
            area = way[2][0]*way[4][0] - way[1][1]*way[3][1]
        else:
            area = way[2][0]*way[4][0] - way[1][0]*way[3][1]
    else:
        if order[:2]==[4,1]:
            area = way[2][0]*way[3][0] - way[4][0]*way[1][0]
        elif order[:3] == [1,4,2]:
            area = way[2][0]*way[3][0] - way[1][0]*way[4][1]
        elif order[:2]==[4,2]:
            area = way[2][0]*way[3][0] - way[1][1]*way[4][1]
        else:
            area = way[2][0]*way[3][0] - way[4][0]*way[1][1]


if len(way[2]) == 2:
    if len(way[4])==2:
        if order[:2]==[2,4]:
            area = way[1][0]*way[3][0] - way[2][0]*way[4][0]
        elif order[:3] == [4,2,3]:
            area = way[1][0]*way[3][0] - way[2][1]*way[4][0]
        elif order[:2]==[2,3]:
            area = way[1][0]*way[3][0] - way[2][1]*way[4][1]
        else:
            area = way[1][0]*way[3][0] - way[2][0]*way[4][1]
    else:
        if order[:2]==[3,2]:
            area = way[1][0]*way[4][0] - way[2][0]*way[3][0]
        elif order[:3] == [2,3,1]:
            area = way[1][0]*way[4][0] - way[2][0]*way[3][1]
        elif order[:2]==[3,1]:
            area = way[1][0]*way[4][0] - way[2][1]*way[3][1]
        else:
            area = way[1][0]*way[4][0] - way[2][1]*way[3][0]      

print(area*n)