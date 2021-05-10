import sys
sys.setrecursionlimit(10**6)
n, m = map(int, sys.stdin.readline().split())
a = [[] for _ in range(n+1)]
for _ in range(m):
  u, v = map(int, sys.stdin.readline().split())
  a[u].append(v)
  a[v].append(u)

check = [False] * (n+1)
check[0] = True


def dfs(x):
  check[x] = True
  for i in a[x]:
    if check[i] == False:
      dfs(i)

ans = 0
for i in range(n+1):
  if not check[i]:
    dfs(i)
    ans += 1
print(ans)
  