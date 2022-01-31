bingo = []
for i in range(5):
    bingo.append(list(map(int,input().split())))

delete = []
cnt = 0


for j in range(5):

    for k in list(map(int,input().split())):
        delete.append(k)

for num in delete:
    
    score = 0

    cnt += 1

    for a in bingo:
        if num in a:

            a.insert(a.index(num), 0)
            a.remove(num)

        if sum(a) == 0:
            score += 1

    for i in range(5):
        if bingo[0][i]==bingo[1][i]==bingo[2][i]==bingo[3][i]==bingo[4][i]:
            score += 1
        
    
    if bingo[0][0]==bingo[1][1]==bingo[2][2]==bingo[3][3]==bingo[4][4]:
        score += 1
        
    if bingo[4][0]==bingo[1][3]==bingo[2][2]==bingo[3][1]==bingo[0][4]:
        score += 1
    
    if score >= 3:
        break

print(cnt)
    

    