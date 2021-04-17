def gcd(x, y) :
  if y == 0 :
    return x
  else :
    return(gcd(y, x%y))

def lcm(x, y, z) :
  l = (x*b)//z
  return(l)

n = int(input())
for _ in range(n) :
  a, b = map(int, input().split())
  g = gcd(a,b)
  l = lcm(a,b,g)
  print(l)
