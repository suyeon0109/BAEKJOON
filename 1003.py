import sys

cnt_0 = [1,0,1,1]+[-1]*37
cnt_1 = [0,1,1,2]+[-1]*37

def fibo_0(n):
  if cnt_0[n] != -1:
    return cnt_0[n]
  else:
    cnt_0[n] = fibo_0(n-1) + fibo_0(n-2)
    return cnt_0[n]

def fibo_1(n):
  if cnt_1[n] != -1:
    return cnt_1[n]
  else:
    cnt_1[n] = fibo_1(n-1) + fibo_1(n-2)
    return cnt_1[n]

for _ in range(int(input())):
  N = int(sys.stdin.readline())
  print(fibo_0(N), fibo_1(N))