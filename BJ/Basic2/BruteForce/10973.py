def next(a):
  # i값은 가장 긴 증가수열의 시작값
  
  for i in range(n-1, -1, -1):
    if i > 0 and a[i] < a[i-1]:
      break
  if i <= 0:
    return False
  print(i)
  

  # j값은 증가수열중에서 i값 앞보다 가장 가장 먼저 작은 값
  for j in range(n-1, 0, -1):
    if a[j] <= a[i-1]:
      break
  print(j)

  # 스왑
  a[i-1], a[j] = a[j], a[i-1]

  # 감소수열 뒤집기
  for k in range(n-1, i, -1):
    a[i], a[k] = a[k], a[i]
    i += 1
    if i >= k:
      break
    

  return True
  
n = int(input())
a = list(map(int, input().split()))
if next(a):
  print(' '.join(map(str,a)))
else:
    print(-1)