from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
  
m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
group = [[-1] * m for _ in range(n)]
q = deque()

for i in range(n):
  for j in range(m):
    if a[i][j] == 1:
      group[i][j] = 0
      q.append((i, j))
while q:
  x, y = q.popleft()
  for i in range(4):
    nx, ny = x+dx[i], y+dy[i]
    if 0 <= nx < n and 0 <= ny < m:
        if a[nx][ny] == 0 and group[nx][ny] == -1:
            q.append((nx,ny))
            group[nx][ny] = group[x][y] + 1
ans = max(map(max, group))
      
for i in range(n):
  for j in range(m):
    if a[i][j] == 0 and group[i][j] == -1:
      ans = -1
print(ans)