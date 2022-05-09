N = int(input())

la = [list(map(str,input())) for _ in range(N)]

cnt_r = 0
cnt_c = 0

for i in la:
    cnt = 0
    for j in range(N):
        if i[j] == 'X':
            if cnt >= 2:
                cnt_r += 1
            cnt = 0
        else:
            cnt += 1
    if cnt >= 2:
        cnt_r += 1
    

for p in range(N):
    cnt = 0
    for q in la:
        if q[p] == 'X':
            if cnt >= 2:
                cnt_c += 1
            cnt = 0
        else:
            cnt += 1
    if cnt >= 2:
        cnt_c += 1

print(cnt_r, cnt_c)