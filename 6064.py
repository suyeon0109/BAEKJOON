# x+M*n = 실제 년 수.
# 이를 N으로 나눈 나머지가 0이면 카잉달력 기준 0이 아닌 N으로 표시되어야 하므로 함수 정의
def calc(n):
    if (x+M*n)%N == 0:
        return N
    else:
        return (x+M*n)%N

for _ in range(int(input())):
    M, N, x, y = map(int, input().split())
    n = 1

    # (x+M*n)%N == x라면 이는 최소공배수를 한번 지났다는 의미이므로 제한조건에 어긋남. -> -1 출력
    while calc(n) != x:
        if calc(n) == y:
            print(x+M*n)
            break
        else:
            n += 1
    else:
        print(-1)