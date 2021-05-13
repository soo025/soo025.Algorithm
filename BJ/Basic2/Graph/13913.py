import sys
from collections import deque
sys.setrecursionlimit(10**9)
MAX = 100000
n, k = map(int, input().split())
check = [False] * (MAX+1)
arr = [-1] * (MAX+1)
ans = [-1] * (MAX+1)
q = deque()
q.append(n)
check[n] = True
arr[n] = 0
ans[n] = 0

while q:
  cur = q.popleft()

  if cur-1 >= 0 and check[cur-1]==False:
    check[cur-1] = True
    arr[cur-1] = arr[cur] + 1
    ans[cur-1] = cur
    q.append(cur-1)

  if cur+1 <= MAX and check[cur+1]==False:
    check[cur+1] = True
    arr[cur+1] = arr[cur] + 1
    ans[cur+1] = cur
    q.append(cur+1)

  if (cur*2) <= MAX and check[cur*2]==False:
    check[cur*2] = True
    arr[cur*2] = arr[cur] + 1
    ans[cur*2] = cur
    q.append(cur*2)

print(arr[k])
def go(n,k):
  if n != k:
    go(n,ans[k])
  print(k, end = ' ')
go(n, k)