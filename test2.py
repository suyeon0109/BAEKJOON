from collections import deque


R = deque()
S = deque()

R.append(1)
S.append(4)
R.extend(S)

print(R)