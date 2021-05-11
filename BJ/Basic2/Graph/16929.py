dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x,y,color,tmp1,tmp2):
  if check[x][y] == True:
    return True
  check[x][y] = True
  for i in range(4):
    nx, ny = x+dx[i], y+dy[i]
    if 0 <= nx < n and 0 <= ny < m:
      if (nx, ny) == (tmp1, tmp2):
        continue
      if a[nx][ny] == color:
        if bfs(nx, ny, color, x, y):
          return True
  return False
  
n, m = map(int, input().split())
a = [input() for _ in range(n)]
check = [[False] * m for _ in range(n)]

for i in range(n):
  for j in range(m):
    if check[i][j]:
      continue
    if bfs(i, j, a[i][j], -1, -1):
      print('Yes')
      exit()
print('No')