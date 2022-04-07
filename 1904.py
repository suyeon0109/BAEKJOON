from collections import deque

n = int(input())
la = deque()
la.append(0)
la.append(1)
la.append(2)
if n > len(la)-1:
  for i in range(len(la),n+1):
    la.append((la[i-1] + la[i-2])%15746)
print(la[n])