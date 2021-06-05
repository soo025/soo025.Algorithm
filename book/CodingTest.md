# 1. 그리디
: 최적의 해인지 `정당성` 검토 필요
ex) 거스름돈 문제, 다익스트라, 크루스칼

> 거스름돈문제(5585)

```python
# 거스름돈
n = 1000 - int(input())
# 동전
coin = [500, 100, 50, 10, 5, 1]
count = 0

for i in coin:
  count += n //i
  n %= i
print(count)
```

---

# 2. 구현
ex) 완전탐색 or 시뮬레이션

> 상하좌우

```python
# 지도크기
n = int(input())
# 시작 위치
x, y = 1, 1
# 이동계획서
plans = input().split()

# 이동방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

# 이동계획 하나씩
for plan in plans:
  for i in range(4):
    if plan == move_type[i]:
      nx = x + dx[i] 
      ny = y + dy[i]

  # 지도를 벗어나는 경우
  if nx < 1 or ny <1 or nx > n or ny > n:
    continue
  # 이동하기
  x, y = nx, ny

print(x, y)
```

---

# 3. DFS
: `스택`, `재귀함수` 사용

```python
# graph는 2차원 연결 리스트로 표현
# visited는 방문된 정보를 1차원 리스트로 표현
# visited = [False] * 9
def dfs(graph, v, visited):
  # 현재 노드 방문 처리
  vistited[v] = True
  print(v, end=' ')
  # 연결된 다른 노드 재귀적으로 방문
  for i in graph[v]:
    if not visted[i]:
      dfs(graph, i, visited)
```

---


# 4. BFS
:`큐` 사용

```python
from collections import deque

def bfs(graph, start, visited):
  # 큐
  queue = deque([start])
  # 현재 노드 방문 처리
  vistied[start] = True
  # 큐가 빌 때까지 반복
  while queue:
    v.queue.popleft()
    print(v, end=' ')
    # 연결된 다른 노드 큐에 삽입
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
```

---

# 5. 정렬

```python
n = int(input())
a = []
for i in range(n):
  input_data = input().split()
  a.append((input_data[0], int(input_data[1])))

a = sorted(a, key=lambda student: student[1])

for student in a:
  print(student[0], end=' ')
```

### * key=lambda

```python
c = sorted(a, key = lambda x : x[0])
# c = [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]
d = sorted(a, key = lambda x : x[1])
# d = [(3, 0), (0, 1), (5, 1), (1, 2), (5, 2)]
```

---

# 6. 이진탐색

: `파라메트릭 서치`(최적화 -> `결정문제`)

> 재귀

```python
def binary_search(a, target, start, end):
  if start > end:
    return None
  mid = (start+end) // 2

  # 찾은 경우
  if a[mid] == target:
    return mid
  elif a[mid] > target:
    return binary_search(a, target, start, mid-1)
  else:
    return binary_search(a, target, mid+1, end)

n, target = map(int, input().split())
a = list(map(int, input().split()))

result = binary_search(a, target, 0, n-1)
if result == None:
  print("찾는 원소가 없습니다")
else:
  print(result+1)
```

> 반복문

```python
def binary_search(a, target, start, end):
  while start <= end:
    mid = (start+end) // 2

    # 찾은 경우
    if a[mid] == target:
      return mid
    elif a[mid] > target:
      end = mid-1
    else:
      start = mid+1

n, target = map(int, input().split())
a = list(map(int, input().split()))

result = binary_search(a, target, 0, n-1)
if result == None:
  print("찾는 원소가 없습니다")
else:
  print(result+1)
```

---

# 7. 다이나믹

> 탑다운(재귀)

```python
d = [0] * 100

def fibo(x):
  if x == 1or x == 2:
    return 1
  # 계산한 문제라면 그대로 반환
  if d[x] != 0:
    return d[x]
  d[x] = fibo(x-1) + fibo(x-2)
  return d[x]

print(fibo(99))
```


---


> 보텀업(반복문)

```python
d = [0] * 199

# 첫번째 피보나치 수와 두번 째 피보나치 수
d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
  d[i] = d[i-1] + d[i-2]

print(d[n])
```


---
