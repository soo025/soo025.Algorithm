import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
set_a = sorted(list(set(a)))
dic = {set_a[i] : i for i in range(len(set_a))}
for i in a:
  print(dic[i], end = ' ')