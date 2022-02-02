list_area = []
for i in range(4):
    x1,y1,x2,y2 = map(int, input().split())

    # x1<x2, y1<y2라는 조건을 전제.
    if x2>x1:
        x1,x2 = x2,x1
    if y2>y1:
        y1,y2 = y2,y1


    # 각 사각형들의 면적이 차지하는 한칸한칸을 성분으로 리스트에 추가.
    # 이를 set로 변환하면, 중복이 삭제.
    for i in range(1, x1-x2+1):
        for j in range(1, y1-y2+1):
            list_area.append((x1-i,y1-j))

print(len(set(list_area)))
