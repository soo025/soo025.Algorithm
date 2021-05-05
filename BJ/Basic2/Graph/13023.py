import sys
def gd(index, cnt):
  # 간선의 개수
  if cnt == 4:
    print(1)
    exit()

  for i in arr[index]:
    if visited[i]:
      continue
    visited[i] = True
    gd(i, cnt + 1)
    visited[i] = False

    
n, m = map(int, input().split())
arr = [[] for _ in range(n)]
for _ in range(m):
  a, b = map(int, sys.stdin.readline().split())
  arr[a].append(b)
  arr[b].append(a)
  
visited = [False] * n

for i in range(n):
  visited[i] = True
  gd(i, 0)
  visited[i] = False
print(0)
