from collections import deque

def cal(k,l):
    global N

    n = 2**N
    ll = 2**l

    if k == 1:

        for i in range(0, n, ll):
            for j in range(0, n, ll):
                lb = [ k[j:j+ll] for k in la[i:i+ll]]
                lb = list(reversed(lb))

                for p in range(ll):
                    for q in range(ll):
                        la[i+p][j+q] = lb[p][q]
        return la

    
    if k == 2:

        for i in range(0, n, ll):
            for j in range(0, n, ll):

                lb = [ k[j:j+ll] for k in la[i:i+ll]]

                for k in range(len(lb)):
                    lb[k] = list(reversed(lb[k]))
                
                for p in range(ll):
                    for q in range(ll):
                        la[i+p][j+q] = lb[p][q]
        return la
    

    if k == 3:

        for i in range(0, n, ll):
            for j in range(0, n, ll):
                lb = [ k[j:j+ll] for k in la[i:i+ll]]
                lc = []

                for item in zip(*lb):
                    lc.append(list(reversed(item)))

                for p in range(ll):
                    for q in range(ll):
                        la[i+p][j+q] = lc[p][q]
        return la
    

    if k == 4:

        for i in range(0, n, ll):
            for j in range(0, n, ll):
                lb = [ k[j:j+ll] for k in la[i:i+ll]]
                lc = deque()

                for item in zip(*lb):
                    lc.appendleft(item)

                for p in range(ll):
                    for q in range(ll):
                        la[i+p][j+q] = lc[p][q]
        return la 
    

    if k == 5:

        lb = [k[:] for k in la]

        for i in range(0, n, ll):
            for j in range(0, n, ll):
                a = n-i-ll
                b = j
                for p in range(ll):
                    for q in range(ll):
                        la[i+p][j+q] = lb[a+p][b+q]
        return la
    

    if k == 6:

        lb = [k[:] for k in la]

        for i in range(0, n, ll):
            for j in range(0, n, ll):
                a = i
                b = n-j-ll
                for p in range(ll):
                    for q in range(ll):
                        la[i+p][j+q] = lb[a+p][b+q]
        return la
    

    if k == 7:

        lb = []

        for a in range(n//ll):
            lb.append([])
            for b in range(n//ll):
                lb[a].append((a,b))

        lc = []
        for item in zip(*lb):
            lc.append(list(reversed(item)))

        ld = [k[:] for k in la]

        for i in range(0, n, ll):
            for j in range(0, n, ll):
                a, b = i//ll, j//ll
                c = ll*lc[a][b][0]
                d = ll*lc[a][b][1]
                for p in range(ll):
                    for q in range(ll):
                        la[i+p][j+q] = ld[c+p][d+q]
        return la
    

    if k == 8:
    
        lb = []

        for a in range(n//ll):
            lb.append([])
            for b in range(n//ll):
                lb[a].append((a,b))

        lc = deque()
        for item in zip(*lb):
            lc.appendleft(item)

        ld = [k[:] for k in la]

        for i in range(0, n, ll):
            for j in range(0, n, ll):
                a, b = i//ll, j//ll
                c = ll*lc[a][b][0]
                d = ll*lc[a][b][1]
                for p in range(ll):
                    for q in range(ll):
                        la[i+p][j+q] = ld[c+p][d+q]
        return la

        

N, R = map(int,input().split())

la = [list(map(int, input().split())) for _ in range(2**N)]

for _ in range(R):
    k,l = map(int, input().split())
    cal(k,l)

for i in la:
    print(*i)