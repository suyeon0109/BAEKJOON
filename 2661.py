N = int(input())

la = ['1','2','3']
num = '1'
ans = '3'*N
def dfs(num):
    global ans
    for a in la:
        flag = 0
        if num[-1] != a:
            num_n = num + a
            for i in range(len(num_n)):
                for j in range(len(num_n)-i-1):
                    if num_n[i-j:i+1] == num_n[i+1:i+2+j]:
                        flag = 1
                        break
                if flag == 1:
                    break
            else:
                num = num_n
                if len(num) == N:
                    if int(ans) > int(num):
                        ans = num
                    return
                dfs(num)
                if ans != '3'*N:
                    return
                num = num[:-1]
dfs(num)
print(ans)