from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

m, n = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
ans = [[-1]*m for _ in range(n)]
ans[0][0] = 0
q = deque()
q.append((0,0))

while q:
  a, b = q.popleft()
  for i in range(4):
    nx, ny = a+dx[i], b+dy[i]
    if 0 <= nx < n and 0 <= ny < m:
      if ans[nx][ny] == -1:
        if arr[nx][ny] == 0:
          ans[nx][ny] = ans[a][b]
          q.appendleft((nx,ny))
        else:
          ans[nx][ny] = ans[a][b] + 1
          q.append((nx,ny))
print(ans[n-1][m-1])