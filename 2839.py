N = int(input())

a = N // 5
b = N % 5
answer = 0

while a >= 0:
    if b%3 == 0:
        answer = a + b//3
        break
    else:
        a -= 1
        b += 5

if a < 0:
    print(-1)
else:
    print(answer)