n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = []

def D(d):
  if len(ans) == m:
    print(' '.join(map(str, ans)))
    return
  over = 0
  for i in range(n):
    if over != a[i]:
      ans.append(a[i])
      over = a[i]
      D(d+1)
      ans.pop()
D(0)