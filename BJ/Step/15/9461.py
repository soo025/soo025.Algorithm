# 1, 1, 1, 2, 2, 3, 4, 5, 7, 9은 n + n+1 = n+3 규칙
MAX = 101
d = [0] * MAX
d[1] , d[2], d[3] = 1, 1, 1
for i in range(0, MAX-3):
  d[i+3] = d[i] + d[i+1]

t = int(input())
for _ in range(t):
  n = int(input())
  print(d[n])
