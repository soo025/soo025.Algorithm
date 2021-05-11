import sys
sys.setrecursionlimit(10**9)
from collections import deque

# 순환
def dfs(s, cur, cnt):
  global cycle
  if s == cur and cnt >= 2:
    cycle = True
    return cycle

  visited[cur] = True
  for i in arr[cur]:
    if not visited[i]:
      dfs(s, i, cnt+1)
    elif s == i and cnt >= 2:
      dfs(s, i, cnt)

# 순환선 사이의 거리
def bfs():
  # q에 순환선의 정점 값 넣기
  q = deque()
  for i in range(n):
    if line[i]:
      vertex[i] = 0
      q.append(i)
  # 순환선과 거리 구하기
  while q:
    c = q.popleft()
    for i in arr[c]:
      if vertex[i] == -1:
        q.append(i)
        vertex[i] = vertex[c] + 1


n = int(input())
arr = [[] for _ in range(n)]
line = [False] * n
vertex = [-1] * n

for i in range(n):
  a, b = map(int, input().split())
  arr[a-1].append(b-1)
  arr[b-1].append(a-1)

for i in range(n):
  visited = [False] * n
  cycle = False
  dfs(i,i,0)
  if cycle:
    line[i] = True
    
bfs()

for i in vertex:
  print(i, end=' ')