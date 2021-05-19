import sys

# 집합의 합, s
s = 0
# 공집합에 추가할 수 있는 경우 20까지
max = 20
m = int(sys.stdin.readline())
for _ in range(m):
  # 문자로, 배열로 입력받음
  op, *num = sys.stdin.readline().split()
  # num을 입력 받으면 x에
  if len(num) > 0:
    x = int(num[0]) - 1
  if op == 'add':
    s = (s | 1<<x)
  elif op == 'remove':
    s = (s & ~(1<<x))
  elif op == 'check':
    r = (s & (1<<x))
    if r > 0:
      sys.stdout.write('1\n')
    else:
      sys.stdout.write('0\n')
  elif op == 'toggle':
    s = (s ^ (1<<x))
  elif op == 'all':
    s = (1 << max) - 1
  else:
    s = 0