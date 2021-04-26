n = 9
a = [int(input()) for _ in range(n)]
a.sort()
s = sum(a)
ans = []

for i in range(0, n-1):
  for j in range(i+1, n):
    if (s - a[i] - a[j]) == 100:
      ans = [i, j]
      break
  if ans:
    break
    
for i in range(0, n):
  if i in ans:
    continue
  print(a[i])
