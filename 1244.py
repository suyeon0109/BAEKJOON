n = int(input())
list_s = list(map(int, input().split()))
stu = int(input())
for i in range(stu):

    list_p = list(map(int, input().split()))

    if list_p[0] == 1:
        for j in range(1,n+1):
            if j % list_p[1] == 0:
                list_s[j-1] = list(set([0,1])-{list_s[j-1]})[0] 

    else:
        j = 1
        while 1:
            try :
                if list_s[list_p[1]-1-j] == list_s[list_p[1]-1+j]:
                    if list_p[1]-1-j < 0:
                        break
                    list_s[list_p[1]-1-j] = list(set([0,1])-{list_s[list_p[1]-1-j]})[0]
                    list_s[list_p[1]-1+j] = list(set([0,1])-{list_s[list_p[1]-1+j]})[0]
                    j += 1
                else:
                    break
            except:
                break
        
        list_s[list_p[1]-1] = list(set([0,1])-{list_s[list_p[1]-1]})[0]


for k in range(len(list_s)):
    list_s[k] = str(list_s[k])

for line in range(1, len(list_s)//20+2):
    try: 
        print(' '.join(list_s[20*(line-1):20*line]))
    except:
        print(' '.join(list_s[20*(line-1):]))

