from collections import deque
dx = [-2,-1,1,2,2,1,-1,-2]
dy = [1,2,2,1,-1,-2,-2,-1]


for tc in range(int(input())):
    I = int(input())
    la = [[0]*I for _ in range(I)]
    s1, s2 = map(int, input().split())
    f1, f2 = map(int, input().split())

    Q = deque()
    Q.append((s1,s2))
    la[s1][s2] = 1

    def move():

        if s1==f1 and s2==f2:
            return 0

        while len(Q):
            s,t = Q.popleft()
            p = la[s][t]

            for i in range(8):
                if 0 <= s+dx[i] <= I-1 and 0 <= t+dy[i] <= I-1 and la[s+dx[i]][t+dy[i]] == 0:
                    Q.append((s+dx[i], t+dy[i]))
                    la[s+dx[i]][t+dy[i]] = p + 1
                    if s+dx[i] == f1 and t+dy[i] == f2:
                        return la[s+dx[i]][t+dy[i]]-1
    
    print(move())