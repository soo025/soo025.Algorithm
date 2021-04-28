n, m = map(int, input().split())
a = []

def D(d):
  if d == m:
    print(' '.join(map(str, a)))
    # 출력 후 함수 반환
    return
  for i in range(1, n+1):
    # 중복되면 제외
    if i in a:
      continue
    a.append(i)
    D(d+1)
    a.pop()
D(0)