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
                t = la[b]
                for j in range(n+1):
                    if la[j] == t:
                        la[j] = la[a]
    
    if c == 1:
        if a == b:
            print('YES')
        elif la[a] == 0 or la[b] == 0 or la[a] != la[b]:
            print('NO')
        else:
            print('YES')
    
    k += 1


# n, m = map(int, input().split())

# la = [i for i in range(n+1)]

# def union(a,b):
#     if a <= b:
#         la[b] = la[a]
#     else:
#         la[a] = la[b]

# def find(a,b):
#     if a <= b:
#         return la[b]
#     if la[a] == la[b]:
#         return 'YES'
#     else:
#         return 'NO'

# for _ in range(m):
#     c, a, b = map(int, input().split())

#     if c == 0:
#         union(a,b)
#     else:
#         print(find(a,b))
    
#     print(la)