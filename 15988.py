from collections import deque
import sys

dp = deque()
dp.append(0)
dp.append(1)
dp.append(2)
dp.append(4)

for _ in range(int(input())):
    n = int(sys.stdin.readline())
    for i in range(len(dp),n+1):
        dp.append((dp[i-1] + dp[i-2] + dp[i-3])%1000000009)
    print(dp[n])