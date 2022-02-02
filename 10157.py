C, R = map(int,input().split())
number = int(input())


x,y = 1,0
cnt = 0
sit = {}
j = 2

while R!=0 and C!=0:

    for k in range(1,R+1):
        cnt +=1
        y += (-1)**j
        sit[cnt]=f'{x} {y}'
  


    for i in range(1,C):
        cnt += 1
        x += (-1)**j
        sit[cnt]=f'{x} {y}'


    j += 1
    C -= 1
    R -= 1

try:
    print(sit[number])
except:
    print('0')