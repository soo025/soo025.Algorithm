t = int(input())
d = []
for _ in range(t):
  n = int(input())
  a = []
  d = [[0]*3 for _ in range(n+1)]
  for _ in range(2):
    a.append(list(map(int, input().split())))
  for i in range(1, n+1):
    d[i][0] = max(d[i-1][1], d[i-1][2])
    d[i][1] = max(d[i-1][0], d[i-1][2]) + a[0][i-1]
    d[i][2] = max(d[i-1][0], d[i-1][1]) + a[1][i-1]
  
  print(max(d[n]))