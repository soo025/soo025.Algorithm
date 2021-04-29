n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
flag = [1] * n
ans = []

def D(d):
  if len(ans) == m:
    print(' '.join(map(str, ans)))
    return
  over = 0
  for i in range(d, n):
    if flag[i] != 0 and over != a[i]:
      ans.append(a[i])
      over = a[i]
      flag[i] = 0
      D(i+1)
      ans.pop()
      flag[i] = 1
D(0)
