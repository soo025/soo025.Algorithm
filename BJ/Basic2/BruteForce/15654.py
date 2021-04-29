n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
b = []

def D(d):
  if d == m:
    print(' '.join(map(str, b)))
    return
  for i in a:
    if i in b:
      continue
    b.append(i)
    D(d+1)
    b.pop()
D(0)