from collections import deque

dx = [ 0, 1, 0, -1]
dy = [1, 0, -1, 0]

r, c = map(int, input().split())
a = [input() for _ in range(r)]
water = [[-1]*c for _ in range(r)]
dist = [[-1] * c for _ in range(r)]
q = deque()

# 시작, 끝, 물 좌표
for i in range(r):
  for j in range(c):
    if a[i][j] == 'S':
      sx, sy = i, j
    elif a[i][j] == 'D':
      ex, ey = i, j
    # 물의 좌표 구하기
    elif a[i][j] == '*':
      water[i][j] = 0
      q.append((i,j))

# water 계산
while q:
  x, y = q.popleft()
  for k in range(4):
    nx, ny = x+dx[k], y+dy[k]
    if 0 <= nx < r and 0 <= ny < c:
      # 물의 좌표일때
      if water[nx][ny] != -1:
        continue
      # 돌, 끝 좌표일때
      if a[nx][ny] == 'X' or a[nx][ny] == 'D':
        continue
      water[nx][ny] = water[x][y] + 1
      q.append((nx,ny))

dist[sx][sy] = 0
q.append((sx,sy))
# dist 계산
while q:
  x, y = q.popleft()
  for k in range(4):
    nx, ny = x+dx[k], y+dy[k]
    if 0 <= nx < r and 0 <= ny < c:
      # 시작 좌표일때
      if dist[nx][ny] != -1:
        continue
      # 돌의 좌표일때
      if a[nx][ny] == 'X':
        continue
      # 물이 먼저 차오를때(단 도착지일때 예외)
      if water[nx][ny] != -1 and dist[x][y] + 1 >= water[nx][ny]:
        continue
      dist[nx][ny] = dist[x][y] + 1
      q.append((nx,ny))

if dist[ex][ey] == -1:
  print('KAKTUS')
else:
  print(dist[ex][ey])