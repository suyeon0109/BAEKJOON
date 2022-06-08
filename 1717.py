n, m = map(int, input().split())
la = [0]*(n+1)

k = 1
for _ in range(m):
    c, a, b = map(int, input().split())

    if c == 0:
        if la[a] == 0:
            if la[b] == 0:
                la[a], la[b] = k, k
            else:
                la[a] = la[b]
        
        else:
            if la[b] == 0:
                la[b] = la[a]
            else:
                for j in range(n+1):
                    if la[j] == la[b]:
                        la[j] = la[a]
    
    if c == 1:
        if a == b:
            print('YES')
        elif la[a] == 0 or la[b] == 0 or la[a] != la[b]:
            print('NO')
        else:
            print('YES')
    
    print(la)
    
    k += 1