def gcd(x, y) :
  if (y == 0):
    return x
  else :
    return gcd(y, x%y)
t = int(input())
for _ in range(t) :
  a = list(map(int, input().split()))
  n = a[0]
  a = a[1:]
  hap = 0
  for i in range(n) :
    for j in range(i+1, n) :
      hap += gcd(a[i], a[j])
  print(hap)
