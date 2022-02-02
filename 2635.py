def minus_number(m):

    # 만들어지는 수의 갯수를 카운트
    cnt = 0
    # 만들어지는 최대수들 리스트
    numbers_final = []

    for x in range(1, m+1):

        numbers = []
        # 나중에 join으로 묶기 위해 문자열로 변환
        numbers.append(str(m))
        numbers.append(str(x))

        while m-x>=0: # 음수가 나오기 전까지만 계속 뺀다.
            numbers.append(str(m-x))
            m, x = x, m-x
        
        # len(numbers): 만들어지는 수들의 갯수
        if cnt < len(numbers):
            cnt = len(numbers)
            numbers_final = numbers

        m = int(numbers[0])

    return numbers_final

n = int(input())

print(len(minus_number(n)))
print(' '.join(minus_number(n)))