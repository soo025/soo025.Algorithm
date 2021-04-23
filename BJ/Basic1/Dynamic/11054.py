n = int(input())
a = list(map(int, input().split()))
d1 = [1] * n
d2 = [1] * n

for i in range(n):
  for j in range(i):
    if a[i] > a[j] and d1[j]+1 > d1[i]:
      d1[i] = d1[j] + 1


for i in range(n-1, -1, -1):
  for j in range(n-1, i-1, -1):
    if a[i] > a[j] and d2[j]+1 > d2[i]:
      d2[i] = d2[j] + 1


d = [d1[i] + d2[i] -1 for i in range(n)]
print(max(d))