lb = []
for i in range(9):
    lb.append(int(input()))
s = sum(lb) - 100

for i in range(len(lb)):
    for j in range(1, len(lb)-i):
        if lb[i] + lb[i+j] == s:
            a, b = lb[i], lb[i+j]
            break

lb.remove(a)
lb.remove(b)
lb.sort()

for i in lb:
    print(i)