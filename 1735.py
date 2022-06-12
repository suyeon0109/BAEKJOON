import math

A,B = map(int, input().split())
C,D = map(int, input().split())

F = math.lcm(B, D)
E = (F//B) * A + (F//D) * C 

G = math.gcd(E, F)
print(E//G, F//G)