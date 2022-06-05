from collections import deque


la = [[1,2,3], [4,5,6], [7,8,9]]
tmp = deque()

for i in zip(*la):
    print(i)
    tmp.appendleft(i)

print(tmp)