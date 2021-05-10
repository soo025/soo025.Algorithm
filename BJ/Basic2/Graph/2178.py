from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]      

def bfs(x, y):
  q = deque()
  q.append((x,y))
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx, ny = x+dx[i], y+dy[i]
      if 0 <= nx < n and 0 <= ny < m:
        if a[nx][ny] == 1 and check[nx][ny] == False:
          q.append((nx,ny))
          group[nx][ny] = group[x][y] + 1
          check[nx][ny] = True
  
n, m = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]
group = [[0] * m for _ in range(n)]
group[0][0] = 1
check = [[False] * m for _ in range(n)]
check[0][0] = True
bfs(0,0)
print(group[n-1][m-1])