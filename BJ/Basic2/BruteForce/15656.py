n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
s = []

def D(d):
  if len(s) == m:
    print(' '.join(map(str, s)))
    return
  for i in range(n):
    s.append(a[i])
    D(d+1)
    s.pop()
D(0)