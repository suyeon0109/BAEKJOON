import sys

def phone(lst):
    for i in range(N-1):
        l = len(lst[i])
        if lst[i+1][:l] == lst[i]:
            return 'NO'
    else:
        return 'YES'

for _ in range(int(input())):
    N = int(sys.stdin.readline())
    la = []
    for _ in range(N):
        la.append(sys.stdin.readline().strip())
    
    la.sort()

    print(phone(la))