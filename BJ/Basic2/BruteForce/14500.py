n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0
tmp = 0
for i in range(n):
  for j in range(m):
    # I 블럭
    if j+3 < m:
      tmp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i][j+3]
      if ans < tmp:
        ans = tmp
    if i+3 < n:
      tmp = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+3][j]
      if ans < tmp:
        ans = tmp

    # O 블럭
    if j+1 < m and i+1 < n:
      tmp = a[i][j] + a[i+1][j] + a[i][j+1] + a[i+1][j+1]
      if ans < tmp:
        ans = tmp

    # L, J 블럭
    # 3 * 2
    if j+1 < m and i+2 < n:
      tmp = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+2][j+1]
      if ans < tmp:
        ans = tmp
      tmp = a[i][j] + a[i+1][j] + a[i+2][j] + a[i][j+1]
      if ans < tmp:
        ans = tmp
      tmp = a[i][j+1] + a[i+1][j+1] + a[i+2][j+1] + a[i+2][j]
      if ans < tmp:
        ans = tmp
      tmp = a[i][j+1] + a[i+1][j+1] + a[i+2][j+1] + a[i][j]
      if ans < tmp:
        ans = tmp
    # 2 * 3
    if j+2 < m and i+1 < n:
      tmp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j]
      if ans < tmp:
        ans = tmp
      tmp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+2]
      if ans < tmp:
        ans = tmp
      tmp = a[i][j] + a[i+1][j] + a[i+1][j+1] + a[i+1][j+2]
      if ans < tmp:
        ans = tmp
      tmp = a[i][j+2] + a[i+1][j] + a[i+1][j+1] + a[i+1][j+2]
      if ans < tmp:
        ans = tmp

    # S, Z 블럭
    # 3 * 2
    if j+1 < m and i+2 < n:
      tmp = a[i][j] + a[i+1][j] + a[i+1][j+1] + a[i+2][j+1]
      if ans < tmp:
        ans = tmp
      tmp = a[i][j+1] + a[i+1][j] + a[i+1][j+1] + a[i+2][j]
      if ans < tmp:
        ans = tmp

    # 2 * 3
    if j+2 < m and i+1 < n:
      tmp = a[i][j] + a[i][j+1] + a[i+1][j+1] + a[i+1][j+2]
      if ans < tmp:
        ans = tmp
      tmp = a[i+1][j] + a[i][j+1] + a[i+1][j+1] + a[i][j+2]
      if ans < tmp:
        ans = tmp
    

    # T 블럭
    # 2 * 3
    if j+2 < m and i+1 < n:
      tmp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+1]
      if ans < tmp:
        ans = tmp
      tmp = a[i+1][j] + a[i+1][j+1] + a[i+1][j+2] + a[i][j+1]
      if ans < tmp:
        ans = tmp

    # 3 * 2
    if j+1 < m and i+2 < n:
      tmp = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+1][j+1]
      if ans < tmp:
        ans = tmp
      tmp = a[i][j+1] + a[i+1][j+1] + a[i+2][j+1] + a[i+1][j]
      if ans < tmp:
        ans = tmp

print(ans)