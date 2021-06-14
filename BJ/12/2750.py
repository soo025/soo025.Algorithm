a = []
n = int(input())
for _ in range(n):
  a.append(int(input()))
a.sort()

for i in range(n):
  print(a[i])
