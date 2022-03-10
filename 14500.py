from copy import deepcopy

def rot(la) :

    rotated = [[] for _ in range(len(la[0]))]
    for i in range(len(la[0])):
        for t in range(len(la)-1,-1,-1):
            rotated[i].append(la[t][i])
    lb = deepcopy(rotated)

    return lb

N, M = map(int, input().split())
la = [list(map(int, input().split())) for _ in range(N)]
sum_max = 0

for _ in range(4):

    # 테트로미노 no.1
    for i in range(len(la)):                # len(la) = 행 개수
        for j in range(len(la[0])-3):       # len(la[0]) = 열 개수
            if sum_max < sum(la[i][j:j+4]):
                sum_max = sum(la[i][j:j+4])

    # no.2
    for i in range(len(la)-1):
        for j in range(len(la[0])-1):
            if sum_max < sum(la[i][j:j+2]+la[i+1][j:j+2]):
                sum_max = sum(la[i][j:j+2]+la[i+1][j:j+2])

    # no.3
    for i in range(len(la)-2):
        for j in range(len(la[0])-1):
            if sum_max < la[i][j]+la[i+1][j]+la[i+2][j]+la[i+2][j+1]:
                sum_max = la[i][j]+la[i+1][j]+la[i+2][j]+la[i+2][j+1]

    # no.3 대칭
    for i in range(len(la)-2):
        for j in range(len(la[0])-1):
            if sum_max < la[i][j+1]+la[i+1][j+1]+la[i+2][j]+la[i+2][j+1]:
                sum_max = la[i][j+1]+la[i+1][j+1]+la[i+2][j]+la[i+2][j+1]
    
    # no.4
    for i in range(len(la)-2):
        for j in range(len(la[0])-1):
            if sum_max < la[i][j]+la[i+1][j]+la[i+1][j+1]+la[i+2][j+1]:
                sum_max = la[i][j]+la[i+1][j]+la[i+1][j+1]+la[i+2][j+1]

    # no.4 대칭
    for i in range(len(la)-2):
        for j in range(len(la[0])-1):
            if sum_max < la[i][j+1]+la[i+1][j]+la[i+1][j+1]+la[i+2][j]:
                sum_max = la[i][j+1]+la[i+1][j]+la[i+1][j+1]+la[i+2][j]

    # no.5
    for i in range(len(la)-1):
        for j in range(len(la[0])-2):
            if sum_max < sum(la[i][j:j+3]) + la[i+1][j+1]:
                sum_max = sum(la[i][j:j+3]) + la[i+1][j+1]
    
    la = rot(la)

print(sum_max)