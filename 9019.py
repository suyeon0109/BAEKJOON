from collections import deque
import sys

# D, S, L, R 계산 함수
def calc(m, num):
    if m == 'D':
        return (num * 2) % 10000
    
    elif m == 'S':
        if num == 0:
            return 9999
        else:
            return num - 1
    
    elif m == 'L':
        return (num % 1000)* 10 + num//1000
    
    else:
        return (num // 10) + (num % 10) * 1000


for _ in range(int(input())):
    visited = [0]*10001
    Q = deque()
    A, B = map(int, sys.stdin.readline().split())

    Q.append([A,''])
    key = ['D','S','L','R']

    flag = 0

    # BFS
    while Q:
        t = Q.popleft()
        for i in range(4):
            ans = calc(key[i],t[0])
            if not visited[ans] :
                Q.append([ans,t[1]+key[i]])
                visited[ans] = 1
            if ans == B:
                print(t[1]+key[i])
                flag = 1
                break
        if flag :
            break