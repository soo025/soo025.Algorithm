def gcd(x, y) :
  if (y == 0) :
    return x
  else :
    return gcd(y, x%y)

n, s = map(int, input().split())
a = list(map(int, input().split()))
a = [abs(s-i) for i in a]
ans = a[0]
for i in range(n) :
  ans = gcd(ans, a[i])
print(ans)
