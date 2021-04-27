def cnt(a):
  max = 1
  for i in range(n):
    cnt = 1
    # 행 계산
    for j in range(1, n):
      if a[i][j] == a[i][j-1]:
        cnt += 1
      else:
        cnt = 1
      if max < cnt:
        max = cnt

    # 열 계산
    cnt = 1
    for j in range(1,n):
      if a[j][i] == a[j-1][i]:
        cnt += 1
      else:
        cnt = 1
      if max < cnt:
        max = cnt
  return max
  
n = int(input())
a = [list(input()) for _ in range(n)]
ans = 0

for i in range(n):
  for j in range(n):
    # 가로 스왑 후 계산
    if j+1 < n:
      a[i][j],a[i][j+1] = a[i][j+1], a[i][j]
      tmp = cnt(a)
      if ans < tmp:
        ans = tmp
      a[i][j],a[i][j+1] = a[i][j+1], a[i][j]

    # 세로 스왑 후 계산
    if i+1 < n:
      a[i][j],a[i+1][j] = a[i+1][j], a[i][j]
      tmp = cnt(a)
      if ans < tmp:
        ans = tmp
      a[i][j],a[i+1][j] = a[i+1][j], a[i][j]

print(ans)