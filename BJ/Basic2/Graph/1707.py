import sys
sys.setrecursionlimit(10**9)
k = int(input())
for _ in range(k):
  v, e = map(int, sys.stdin.readline().split())
  a = [[] for _ in range(v+1)]
  for _ in range(e):
    e1, e2 = map(int, sys.stdin.readline().split())
    a[e1].append(e2)
    a[e2].append(e1)
  color = [0] * (v+1)

  def dfs(x, y):
    color[x] = y
    for i in a[x]:
      if color[i] == 0:
        dfs(i, 3-y)
  ans = True
  for i in range(1, v+1):
    if color[i] == 0:
      dfs(i, 1)
  for i in range(1, v+1):
    for j in a[i]:
      if color[i] == color[j]:
        ans = False
  print('YES' if ans else 'NO')