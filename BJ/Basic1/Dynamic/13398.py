n = int(input())
a = list(map(int, input().split()))
d1 = [0] * n
d2 = [0] * n

for i in range(n):
  if i==0:
    d1[i] = a[i]
  else:
    d1[i] = max(a[i], d1[i-1] + a[i])

for i in range(n-1, -1, -1):
  if i == n-1:
    d2[i] = a[i]
  else:
    d2[i] = max(a[i], d2[i+1] + a[i])

ans = max(d1)
for i in range(1, n-1):
  ans = max(ans, d1[i-1]+d2[i+1])
print(ans)