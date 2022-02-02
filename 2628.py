# 종이의 넓이와 높이 설정
width, height = map(int,input().split())

# 자르는 횟수 설정
n = int(input())
list_line = []

# 가로와 세로, 자르는선 번호 설정하여 튜플형태로 리스트 list_line에 추가.
for i in range(n):
    a,b = map(int, input().split())
    list_line.append((a,b))

# 만들어진 list_line을 튜플의 value 값 기준으로 정렬. (오름차순)
# 이를 lines라는 새로운 리스트로 정의
lines = sorted(list_line, key = lambda x: x[1])


h = 0
w = 0
list_height = []
list_width = []
for line in lines:                    # # lines 리스트에서 for문을 돌리면서
    if line[0] == 0:                  # 1) 가로 혹은 세로를 판별
        list_height.append(line[1]-h) # 2) 작은 점선번호부터 자른다. -> 조각의 길이가 정해진다.
        h = line[1]
    else:
        list_width.append(line[1]-w)
        w = line[1]
list_height.append(height-h)   # 3) 생성된 조각의 길이를 새로운 리스트 list_height, list_width에 저장.
list_width.append(width-w)

# 조각의 길이들을 이용해 각각의 조각의 넓이를 구해
# 새로운 넓이 리스트 list_area에 저장
list_area = []
for i in list_height:
    for j in list_width:
        list_area.append(i*j)

# 넓이들 중 최댓값을 출력
print(max(list_area))

