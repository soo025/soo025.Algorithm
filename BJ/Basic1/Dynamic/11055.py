n = int(input())
a = list(map(int, input().split()))
d = [0]  n
d[0] = a[0]

for i in range(n)
  for j in range(i)
    if a[i]  a[j]
      d[i] = max(d[i], d[j]+a[i])
    else
      d[i] = max(d[i], a[i])
print(max(d))