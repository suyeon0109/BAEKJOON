import sys

for _ in range(int(input())):
  tri = [0,1,1,1,2,2,3,4,5,7,9,12]
  N = int(sys.stdin.readline())
  if N > 11:
    for i in range(12,N+1):
      tri.append(tri[i-5] + tri[i-1])
  print(tri[N])