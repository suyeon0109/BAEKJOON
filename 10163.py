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
           
l1 = list(d1.values())
print(l1)
for i in range(T):
    print(l1.count(i))


