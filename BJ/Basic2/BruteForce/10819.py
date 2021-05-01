def per(a):
  n = len(a)-1
  for i in range(n, -1, -1):
    if a[i] > a[i-1]:
      break

  if i <= 0:
    return False

  for j in range(n, 0, -1):
    if a[j] > a[i-1]:
      break

  a[i-1], a[j] = a[j], a[i-1]

  while i < n:
    a[i], a[n] = a[n], a[i]
    i += 1
    n -= 1

  return True
    
def cnt(a):
  tmp = 0
  for i in range(1, len(a)):
    tmp += abs(a[i] - a[i-1])
  return tmp

n = int(input())
a = list(map(int, input().split()))
a.sort()
result = 0
ans = 0
while True:
  result = cnt(a)
  ans = max(result, ans)
  if not per(a):
    break

print(ans)