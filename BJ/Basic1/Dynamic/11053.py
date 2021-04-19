n = int(input())
d= [1] * n
a = list(map(int, input().split()))

for i in range(n):
  for j in range(i):
    if a[i] > a[j] and d[i] < d[j] + 1:
      d[i] = d[j] + 1
print(max(d))
