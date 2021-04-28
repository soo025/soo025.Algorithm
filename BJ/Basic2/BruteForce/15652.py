n, m = map(int, input().split())
a = []

def D(d):
  if len(a) == m:
    print(' '.join(map(str, a)))
    return
  for i in range(d-1, n):
    a.append(i+1)
    D(i+1)
    a.pop()
D(1)