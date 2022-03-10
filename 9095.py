# 0 -> 1
# 1 -> 1개
# 2 -> 2개
# 3 -> 4개
# 4 -> 7개
# 5 -> 13개

la = [0,1,2,4]
def add_123(n):
    if len(la) > n:
        return la[n]
    else:
        la.append(add_123(n-3)+add_123(n-2)+add_123(n-1))
        return la[n]

for _ in range(int(input())):
    print(add_123(int(input())))
