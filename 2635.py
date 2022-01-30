def minus_number(m):
    cnt = 0
    numbers_final = []

    for x in range(1, m+1):
        numbers = []
        numbers.append(str(m))

        numbers.append(str(x))

        while m-x>=0:
            numbers.append(str(m-x))
            m, x = x, m-x
        
        if cnt < len(numbers):
            cnt = len(numbers)
            numbers_final = numbers
        m = int(numbers[0])

    return numbers_final

n = int(input())

print(len(minus_number(n)))
print(' '.join(minus_number(n)))