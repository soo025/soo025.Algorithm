n, k = map(int, input().split())
d = [[0] * (n+1) for _ in range(k+1)]

for i in range(1, k+1):
  for j in range(1, n+1):
    if i == 1:
      d[i][j] = 1
    elif j == 1:
      d[i][j] = i    
    else:
      d[i][j] = (d[i][j-1] + d[i-1][j]) % 1000000000
print(d[k][n])