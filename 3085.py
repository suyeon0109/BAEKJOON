n = int(input())
la = [list(map(str, input())) for _ in range(n)]
c_max = 1

for i in range(n):
    for j in range(n-1):

        if la[i][j] != la[i][j+1]:
            la[i][j], la[i][j+1] = la[i][j+1], la[i][j]

            for k in range(n):
                c = 1
                for l in range(n-1):
                    if la[k][l] == la[k][l+1]:
                        c += 1
                        if c_max < c:
                            c_max = c
                    else:
                        c = 1
            
            for l in range(n):
                c = 1
                for k in range(n-1):
                    if la[k][l] == la[k+1][l]:
                        c += 1
                        if c_max < c:
                            c_max = c
                    else:
                        c = 1
            
            la[i][j], la[i][j+1] = la[i][j+1], la[i][j]

for j in range(n):
    for i in range(n-1):
        if la[i][j] != la[i+1][j]:
            la[i][j], la[i+1][j] = la[i+1][j], la[i][j]

            for k in range(n):
                c = 1
                for l in range(n-1):
                    if la[k][l] == la[k][l+1]:
                        c += 1
                        if c_max < c:
                            c_max = c
                    else:
                        c = 1
            
            for l in range(n):
                c = 1
                for k in range(n-1):
                    if la[k][l] == la[k+1][l]:
                        c += 1
                        if c_max < c:
                            c_max = c
                    else:
                        c = 1
            
            la[i][j], la[i+1][j] = la[i+1][j], la[i][j]

print(c_max)