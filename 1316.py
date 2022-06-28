n = int(input())
cnt = 0

for _ in range(n):
    alph = [0]*26
    word = input()

    for i in range(len(word)):
        if alph[ord(word[i])-97] == 0:
            alph[ord(word[i])-97] = 1
        elif word[i] == word[i-1]:
            continue
        else:
            break
    else:
        cnt += 1

print(cnt)