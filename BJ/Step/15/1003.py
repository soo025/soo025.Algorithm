t = int(input())
# 피보나치 수열로 증가함
for _ in range(t):
  n = int(input())
  zero = 1
  one = 0
  tmp = 0
  for _ in range(n):
    tmp = one
    one += zero
    zero = tmp
  print(zero, one)
