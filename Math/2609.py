def gcd(x, y) :
  if y == 0 :
    return x
  else :
    return(gcd(y, x%y))

def lcm(x, y, z) :
  n = (x*b)//z
  return(n)
  
a, b = map(int, input().split())
g = gcd(a,b)
l = lcm(a,b,g)
print(g)
print(l)
