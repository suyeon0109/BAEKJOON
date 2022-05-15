import sys

# 전화번호들 번호순으로 나열.
# 길이가 짧은 번호부터 조회
# 해당 순서의 번호가 그 다음 순서의 번호에 포함 되는지 확인.
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