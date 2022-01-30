n = int(input())

dict_s = {}

# 딕셔너리 dict_s에 기둥왼쪽면:기둥높이 를 입력값으로 추가 
for i in range(n):
    a,b = map(int,input().split())
    dict_s[a] = b

# 기둥들을 기둥왼쪽면 번호 기준으로 정렬하고, 리스트로 만든다.
col = list(sorted(zip(dict_s.keys(), dict_s.values())))

max_c = max(zip(dict(col).values(), dict(col).keys()))


while 1 :
    # col_d -> 기둥이 양쪽옆 기둥보다 높이가 작으면, 전체 면적에 영향을 안준다.
    #          따라서 해당하는 기둥들은 삭제해도 무방
    #          이렇게 삭제할 기둥들을 추가할 리스트가 col_d
    col_d =[]
    for i in range(len(col)):
        try:
            # 양쪽 옆 기둥보다 작을 때
            if col[i][1] <= col[i+1][1] and col[i][1] <= col[i-1][1]: 
                if i-1 <0: # 인덱스가 음수가 나오는것을 방지
                    pass
                else:
                    col_d.append(col[i])
                  
        except:
            pass

    # 기존 기둥들에서 col_d에 추가한 기둥들을 삭제. (set 이용)
    q = dict(set(col) - set(col_d)) 

    # 수정된 기둥 리스트를 키값(기둥 왼쪽면)으로 정렬
    col = list(sorted(zip(q.keys(), q.values()))) 

    # 오목한 부분이 나오지 않을떄 까지, 이 과정을 반복.
    # 더이상 삭제될 기둥이 없을 때, 반복 종료
    if len(col_d) ==0:
        break

# 남은 기둥들 중 최대 높이인 기둥을 찾는다.
max_c = max(zip(dict(col).values(), dict(col).keys()))

# 전체가로길이 * 기둥최대높이 로 전체사각형 면적 구한다.
entire = (col[-1][0]+1-col[0][0]) * max_c[0]

# 전체 사각형 entire에서 뺄 부분을 정해서 뺀다.
for i in range(len(col)):
    try:
        if max_c[1] < col[i][0]: # 기둥이 제일 큰 기둥보다 오른쪽에 있을 때.
            entire -= (max_c[0] - col[i][1]) * abs(col[i-1][0]-col[i][0])
        else:                    # 기둥이 제일 큰 기둥보다 왼쪽에 있을 때.
            entire -= (max_c[0] - col[i][1]) * abs(col[i+1][0]-col[i][0])
    except :
        pass

print(entire)