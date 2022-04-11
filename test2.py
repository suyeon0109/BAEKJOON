from collections import deque

def BFS(arr, n, k):
    que = deque()
    que.append((n, [n]))

    while que:
        mn, ord = que.popleft()

        if mn == k:
            return arr[mn], ord

        for next_n in [2*mn, mn+1, mn-1]:
            if 0 <= next_n < 100001 and arr[next_n] == -1:
                arr[next_n] = arr[mn] + 1
                que.append((next_n, ord+[next_n]))


N, K = map(int, input().split())
loc = [-1] * 100001
loc[N] = 0

ans, order = BFS(loc, N, K)
print(ans)
print(*order)
