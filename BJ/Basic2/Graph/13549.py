from collections import deque
MAX = 100000
check = [False] * (MAX+1)
arr = [-1] * (MAX+1)
n, k = map(int, input().split())
check[n] = True
arr[n] = 0
q = deque()
q.append(n)

while q:
  cur = q.popleft()
  
  if cur*2 <= MAX and check[cur*2] == False:
    check[cur*2] = True
    arr[cur*2] = arr[cur]
    q.append(cur*2)

  if cur-1 >= 0 and check[cur-1] == False:
    check[cur-1] = True
    arr[cur-1] = arr[cur] + 1
    q.append(cur-1)

  if cur+1 <= MAX and check[cur+1] == False:
    check[cur+1] = True
    arr[cur+1] = arr[cur] + 1
    q.append(cur+1)

print(arr[k])