from collections import deque

A, P = map(str, input().split())
P = int(P)
la = [0]*((9**P)*4 + 1)
lb = deque()

la[int(A)] = 1
lb.append(A)
t = 0

while 1:
    summ = 0
    for i in range(len(lb[t])):
        summ += int(lb[t][i]) ** P
    if la[summ] == 1:
        lb = list(lb)[:lb.index(str(summ))]
        break
    lb.append(str(summ))
    la[summ] = 1
    t += 1

print(len(lb))