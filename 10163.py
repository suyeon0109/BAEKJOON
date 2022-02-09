T = int(input())
d1 = {}

for i in range(T):
    a,b,c,d = map(int, input().split())
    for j in range(c):
        for k in range(d):
            if a+j > 1000 or b+k > 1000:
                pass
            else:
                d1[(a+j,b+k)] = i

# d1 = {(0,0) : 0, (0,1) : 0,  ,,,  (3,3) : 1,  ,,,, }
for m in range(T):
    cnt = 0
    for key, value in d1.items():
        if value == m:
            cnt += 1
    print(cnt)


