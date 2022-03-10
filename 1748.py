n = int(input())

# 15 -> 1*9 + 2*6 = 21
# 120 -> 1*9 + 2*90 + 3*21 = 252

m_sum = 0
l = 1
while l < len(str(n)):
    m_sum += l * 9 * (10 ** (l-1))
    l += 1
m_sum += (n - (10**(l-1)-1)) * l

print(m_sum)