n, k = map(int, input().split())
money = []
ans = 0
for i in range(n):
  money.append(int(input()))
for i in range(n-1, -1, -1):
  if k == 0:
    break
  if money[i] > k:
    continue
  ans += k // money[i]
  k %= money[i]
print(ans)
