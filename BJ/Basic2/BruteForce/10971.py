import sys

def df(cur, cost):
  global n, a, v, m
  if cost < m:
    if all(v) and cur == 0:
      m = min(cost, m)
    for i in range(n):
      if a[cur][i] > 0 and not v[i]:
        v[i] = 1
        df(i, cost+a[cur][i])
        v[i] = 0

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
v = [0] * n
m = sys.maxsize
df(0,0)
print(m)
