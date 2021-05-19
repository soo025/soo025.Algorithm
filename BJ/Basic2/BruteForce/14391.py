n, m = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]
ans = 0
# 경우의 수가 2^n*m
for s in range(1<<(n*m)):
  sum = 0
  
  # 가로합
  for i in range(n):
    rowsum = 0
    for j in range(m):
      index = i * m + j
      # 가로
      if (s & (1 << index)) == 0:
        rowsum = rowsum * 10 + a[i][j]
      # 세로
      else:
        sum += rowsum
        rowsum = 0
    sum += rowsum


  # 세로합
  for i in range(m):
    colsum = 0
    for j in range(n):
      index = j * m + i
      # 세로
      if (s & (1 << index)) != 0:
        colsum = colsum * 10 + a[j][i]
      # 가로
      else:
        sum += colsum
        colsum = 0
    sum += colsum
  ans = max(ans, sum)
print(ans)