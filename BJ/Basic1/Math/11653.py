n = int(input())
i = 2


while n >= i*i :
  while n % i == 0 :
    print(i)
    n //= i
  i += 1
if n > 1:
  print(n)
