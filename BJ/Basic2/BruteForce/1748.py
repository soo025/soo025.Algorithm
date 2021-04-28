n = int(input())
ans = 0
a = 0


for i in range(len(str(n))):
  #마지막에는 n-((10**i)-1)로 나머지를 계산
  if i+1 == len(str(n)):
    a = (n - ((10 ** i)-1)) * (i+1)
  else:
    ans += ((10 ** (i+1)) - (10 ** i)) * (i+1)
ans += a
print(ans)