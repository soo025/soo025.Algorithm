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



# 8. 최단경로 - 다익스트라
: `인접리스트`, 노드의 개수가 `많은` 경우

: 우선순위 큐(heapq 라이브러리)
```python
import heapq
import sys
input = sys.stdin.readline
INF = int(10**9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

# 간선 정보 입력받기
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b,c))

def dijkstra(start):
  q = []
  # 시작 노드
  heapq.heappush(q, (0,start))
  distance[start] = 0
  
  while q:
    # 거리와 노드
    dist, now = heapq.heappop(q)
    # 이미 처리된 노드
    if distance[now] < dist:
      continue
    # 현재 노드와 연결된 노드의 거리
    for i in graph[now]:
      cost = dist + i[1]
      # 더 짧은 경우
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost,i[0]))

dijkstra(start)

for i in range(1, n+1):
  if distance[i] == INF:
    print("INFINITY")
  else:
    print(distance[i])
```

# 9. 최단경로 - 플로이드 워셜
: `인접 행렬`, 노드의 개수가 `적은` 경우

```python
INF = 10**9

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

# 자신에게 가는 비용, 0으로
for i in range(1, n+1):
  for j in range(1, n+1):
    if i == j:
      graph[i][j] = 0

# 간선 정보
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a][b] = c

# 플로이드 워셜 알고리즘
for i in range(1, n+1):
  for j in range(1, n+1):
    for k in range(1, n+1):
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n+1):
  for j in range(1, n+1):
    if graph[i][j] == INF:
      print("INFINITY", end= " ")
    else:
      print(graph[i][j], end=" ")
  print()
```

---

# 10. 서로소 집합(유니온 파인드)

```python
# 루트 노드 찾기
def find_parent(parent, x):
  # 루트 노드 찾을 때까지 재귀적 호출
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  # 루트 노드라면 경로압축으로 부모 테이블값 갱신
  return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  # 작은 쪽이 루트 노드
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

# 노드의 개수와 개수
v, e = map(int, input().split())

# 부모 테이블 자기 자신으로 초기화
parent = [0]*(v+1)
for i in range(1, v+1):
  parent[i] = i

# union 연산
for i in range(e):
  a, b = map(int, input().split())
  union_parent(parent, a, b)


# 각 원소가 속한 집합
print('각 원소가 속한 집합: ', end='')
for i in range(1, v+1):
  print(find_parent(parent, i), end=' ')
print()
# 부모 테이블
print('부모 테이블: ', end='')
for i in range(1, v+1):
  print(parent[i],end=' ')
```


---


# 11. 크루스칼
: 사이클이 없는 최소 스패닝 트리

```python
# 루트 노드 찾기
def find_parent(parent, x):
  # 루트 노드 찾을 때까지 재귀적 호출
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  # 루트 노드라면 경로압축으로 부모 테이블값 갱신
  return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  # 작은 쪽이 루트 노드
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

# 노드의 개수와 개수
v, e = map(int, input().split())

# 부모 테이블 자기 자신으로 초기화
parent = [0]*(v+1)
for i in range(1, v+1):
  parent[i] = i

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 간선 입력
for _ in range(e):
  a, b, cost = map(int, input().split())
  # 튜플의 첫번째 원소가 정렬 기준이므로 cost를 처음으로 추가
  edges.append((cost, a, b))
edges.sort()

# 간선 확인
for edge in edges:
  cost, a, b = edge
  # 사이클이 발생하지 않는다면 집합 포함
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost
print(result)
```

---


# 12. 위상정렬
: 방향그래프의 모든 노드를 `순서대로` 나열

```python
from collections import deque

# 노드 개수와 간선
v, e = map(int, input().split())
# 노드의 진입 차수 초기화
indegree = [0] * (v+1)
graph = [[] for i in range(v+1)]

# 방향 그래프의 간선 입력, 진입 차수 추가
for _ in range(e):
  a, b = map(int, input().split())
  graph[a].append(b)
  indegree[b] += 1

# 위상정렬
def topology_sort():
  result = []
  q = deque()
  # 1. 진입 차수 0인 노드 큐에 삽입
  for i in range(1, v+1):
    if indegree[i] == 0:
      q.append(i)

  # 2. 큐가 빌 때까지 반복
  while q:
    # 2-1. 큐에서 원소 빼고 result에 넣기
    now = q.popleft()
    result.append(now)
    # 2-2. 뺀 원소의 진입차수 1 빼기
    for i in graph[now]:
      indegree[i] -= 1
      # 2-3. 진입차수가 0이라면 큐에 삽입
      if indegree[i] == 0:
        q.append(i)
        
  for i in result:
    print(i, end=' ')

topology_sort()
```

