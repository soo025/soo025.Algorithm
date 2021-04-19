MAX = 1000000
check = [False] * (MAX+1)
prime = []

for i in range(2, MAX+1) :
  if check[i] == False:
    prime.append(i)
    j = i + i
    while j <= MAX :
      check[j] = True
      j += i

t = int(input())
for _ in range(t):
  n = int(input())
  ans = 0
  for i in prime :
    if n-i >= i:
      if check[n-i] == False :
        ans += 1
    else :
      break
  print(ans)
