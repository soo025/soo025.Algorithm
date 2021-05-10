from collections import deque
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

def dfs(x, y, cnt):
  group[x][y] = cnt
  q = deque()
  q.append((x,y))
  while q:
    x, y = q.popleft()
    for i in range(8):
      nx, ny = x+dx[i], y+dy[i]
      if 0 <= nx < h and 0 <= ny < w:
        if a[nx][ny] == 1 and group[nx][ny] == 0:
          group[nx][ny] = cnt
          q.append((nx,ny))
  
while True:
  w, h = map(int, input().split())
  if w == 0 and h == 0:
    break
  a = [list(map(int, input().split())) for _ in range(h)]
  group = [[0] * w for _ in range(h)]
  cnt = 0
  for i in range(h):
    for j in range(w):
      if a[i][j] == 1 and group[i][j] == 0:
        cnt += 1
        dfs(i, j, cnt)
  print(cnt)