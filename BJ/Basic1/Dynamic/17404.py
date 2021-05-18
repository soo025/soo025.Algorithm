import sys
ans = sys.maxsize
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
d = [[0,0,0] for _ in range(n)]

for index in range(3):
  # 첫번째 집 색 고정
  for i in range(3):
    if index == i:
      d[0][i] = a[0][i]
    else:
      d[0][i] = ans
  
  # 계산
  for i in range(1, n):
    d[i][0] = min(d[i-1][1], d[i-1][2]) + a[i][0]
    d[i][1] = min(d[i-1][0], d[i-1][2]) + a[i][1]
    d[i][2] = min(d[i-1][0], d[i-1][1]) + a[i][2]

  for i in range(3):
    # 첫번째와 n번째 집이 같은 색인 경우
    if index == i:
      continue
    ans = min(ans, d[n-1][i])
print(ans)