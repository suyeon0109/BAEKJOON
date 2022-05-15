import sys

input = sys.stdin.readline

# 테스트케이스 개수를 정확히 모르므로 try except
# 투포인터 방법
while 1:
    try:
        x = int(input())
        x *= 10**7          # cm -> nm 변환
        n = int(input())
        la = [int(input()) for _ in range(n)]
        la.sort()           # 레고를 크기순으로 나열

        l1, l2 = 0, 0

        start, end = 0, n-1 # 처음과 끝에 두 포인터를 놓고, 
                            # 두 포인터가 가리키는 레고 크기의 합에 따라 포인터를 이동

        while start < end:
            if la[start] + la[end] == x:
                l1, l2 = la[start], la[end]
                break
            elif la[start] + la[end] > x:
                end -= 1
            else:
                start += 1
        
        if l1 == 0 and l2 == 0:
            print('danger')
        else:
            print('yes', l1, l2)
    except:
        break