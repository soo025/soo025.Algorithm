def p(n):
  if n <=1:
    return n
  return p(n-1) + p(n-2)

n = int(input())
print(p(n))
