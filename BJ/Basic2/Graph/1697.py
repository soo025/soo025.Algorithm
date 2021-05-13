from collections import deque

MAX = 100000
check = [False] * (MAX +1)
a = [-1] * (MAX + 1)
q = deque()

n , m = map(int, input().split())
check[n] = True
q.append(n)
a[n] = 0

while q:
  cur = q.popleft()
  for i in [cur-1, cur+1, cur*2]:
    if 0 <= i <= MAX and check[i] == False:
      check[i] = True
      a[i] = a[cur] + 1
      q.append(i)
print(a[m])