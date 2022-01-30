dices = []
n = int(input())

for i in range(n):
    d1 = {}
    face = ['A','B','C','D','E','F']
    k = 0
    for j in list(map(int,input().split())):
        d1[face[k]] = j
        k += 1
    dices.append(d1)

def del_face(f):
    if f=='A':
        return 'F'
    elif f=='B':
        return 'D'
    elif f=='C':
        return 'E'
    elif f=='D':
        return 'B'
    elif f=='E':
        return 'C'
    elif f=='F':
        return 'A'

list_max = []

for i in face:

    s = 0

    delete = dices[0][del_face(i)]
    s += max(zip(dict(dices[0].items() - {(i, dices[0][i])} - {(del_face(i),dices[0][del_face(i)])}).values(), dict(dices[0].items() - {(i, dices[0][i])} - {(del_face(i),dices[0][del_face(i)])}).keys()))[0]

    for dice in dices[1:]:
        for j in face:
            try :
                if dice[j] == delete:
                    delete = dice[del_face(j)]
                    s += max(zip(dict(dice.items() - {(j, dice[j])} - {(del_face(j),dice[del_face(j)])}).values(), dict(dice.items() - {(j, dice[j])} - {(del_face(j),dice[del_face(j)])}).keys()))[0]
                    break
            except:
                pass
    
    list_max.append(s)


print(max(list_max))