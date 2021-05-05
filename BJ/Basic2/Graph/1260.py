from collections import deque

def dfs(index):
  print(index, end=' ')
  check[index] = True
  for i in arr[index]:
    if check[i] == False:
      dfs(i)

def bfs(index):
  dq = deque()
  dq.append(index)
  check[index] = True
  while dq:
    x = dq.popleft()
    print(x, end=' ')
    for i in arr[x]:
      if check[i] == False:
        check[i] = True
        dq.append(i)
        
  

n , m, v = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  arr[a].append(b)
  arr[b].append(a)
for i in range(n):
  arr[i].sort()
  

check = [False] * (n+1)
dfs(v)
print()
check = [False] * (n+1)
bfs(v)
print()