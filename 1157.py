word = input()

alpha = [0]*26

for i in range(len(word)):
    if word[i].islower():
        alpha[ord(word[i])-32-65] += 1
    else:
        alpha[ord(word[i])-65] += 1

if alpha.count(max(alpha)) > 1:
    print('?')
else:
    print(chr(alpha.index(max(alpha)) + 65))