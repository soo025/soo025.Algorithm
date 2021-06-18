import sys
n = int(sys.stdin.readline())
a = []
for _ in range(n):
  a.append(sys.stdin.readline().rstrip())
# 중복제거
a = list(set(a))
a.sort(key=lambda x : (len(x), x))
for i in a:
  print(i)