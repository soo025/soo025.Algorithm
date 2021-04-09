def fac(n) :
  a = 0
  i = d = 5
  while i <= n :
    a += n//i
    i *= d
  return a

n = int(input())
ans = fac(n)
print(ans)
