N = int(input())

for _ in range(N):
    sen = input()
    score_sum = 0
    score = 0
    t = 1
    for i in range(len(sen)):
        if sen[i] == 'O':
            score += t
            t += 1
            if i == len(sen)-1:
                score_sum += score
        else:
            score_sum += score
            t = 1
            score = 0
    print(score_sum)