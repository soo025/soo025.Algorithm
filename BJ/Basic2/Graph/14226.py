from collections import deque

s = int(input())
e = [[-1] * (s+1) for _ in range(s+1)]
q = deque()
q.append((1,0))
e[1][0] = 0

while q:
  a, b = q.popleft()

  # 복사
  if e[a][a] == -1:
    e[a][a] = e[a][b] + 1
    q.append((a,a))

  # 붙여넣기, if 조건문 순서 조심
  if a+b <= s and e[a+b][b] == -1:
    e[a+b][b] = e[a][b] + 1
    q.append((a+b,b))

  # 삭제
  if a-1 >= 0 and e[a-1][b] == -1:
    e[a-1][b] = e[a][b] + 1
    q.append((a-1, b))

ans = min([i for i in e[s] if i != -1])
print(ans)