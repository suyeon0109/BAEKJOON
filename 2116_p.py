dices = []
n = int(input())

for i in range(n):
    dices.append(dict(enumerate(map(int,input().split()))))
    # [ {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6}, {0: 6, 1: 5, 2: 4, 3: 3, 4: 2, 5: 1}, ,,,,,]

def delete_face(n):
    if n==0:
        return 5
    elif n==1:
        return 3
    elif n==2:
        return 4
    elif n==3:
        return 1
    elif n==4:
        return 2
    elif n==5:
        return 0


list_max = []

for i in range(6):

    s = 0
    dice_n = dices[0].items()
    for key, value in dices[0].items():
        if key == i or key == delete_face(i):
            dice_n = dice_n - {(key, value)}
    s += max(zip(dict(dice_n).values(), dict(dice_n).keys()))[0]


    try:
        dice_n = dices[1].items()
        for key, value in dices[1].items():
            if value == dices[0][delete_face(i)]:
                a = dices[1][delete_face(key)]
                dice_n = dice_n -{(key, value)} - {(delete_face(key),a)}
        s += max(zip(dict(dice_n).values(), dict(dice_n).keys()))[0]


        for j in range(2,n):
            dice_n = dices[j].items()
            for key, value in dices[j].items():
                if value == a:
                    a = dices[j][delete_face(key)]
                    dice_n = set(dices[j].items())-{(key, value)} - {(delete_face(key),a)}
            s += max(zip(dict(dice_n).values(), dict(dice_n).keys()))[0]


    except:
        pass
    
    
    list_max.append(s)


print(max(list_max))





for j in dice:
        if dice[j] == delete:
            del dice[j]
            delete = dice[del_face[j]]
            del dice[del_face[j]]
    s += max(zip(dice.values(), dice.keys()))

    for k in dices[2]:
        if dices[2][k] == delete:
            del dices[2][k]
            delete = dices[2][del_face[k]]
            del dices[2][del_face[k]]
    s += max(zip(dice.values(), dice.keys()))
   

    











