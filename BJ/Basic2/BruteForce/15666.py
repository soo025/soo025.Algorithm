n, m = map(int, input().split())
a = list(map(int, input().split()))
a = list(set(a))
a.sort()
ans = []

def D(d):
  if len(ans) == m:
    print(' '.join(map(str, ans)))
    return
  for i in range(d-1, len(a)):
    ans.append(a[i])
    D(i+1)
    ans.pop()
D(1)