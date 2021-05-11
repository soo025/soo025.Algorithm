from collections import deque

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(n1, n2, m1, m2):
  q = deque()
  q.append((n1,n2))
  group[n1][n2] = 0
  while q:
    x, y = q.popleft()
    if x == m1 and y == m2:
      print(group[m1][m2])
      return
    for i in range(8):
      nx, ny = x+dx[i], y+dy[i]
      if 0 <= nx < l and 0 <= ny < l:
        if group[nx][ny] == -1:
          q.append((nx,ny))
          group[nx][ny] = group[x][y] + 1

t = int(input())
for _ in range(t):
  l = int(input())
  n1, n2 = map(int, input().split())
  m1, m2 = map(int, input().split())
  group = [[-1] * l for _ in range(l)]
  bfs(n1,n2,m1,m2)