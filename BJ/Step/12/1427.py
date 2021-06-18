import sys
n = sys.stdin.readline().rstrip()
n = [int(i) for i in n]
n.sort(reverse=True)
for i in n:
  print(i, end='')