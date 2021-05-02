import sys

def lotto(index, s, visited, ans):
  if len(ans) == 6:
    print(' '.join(map(str, ans)))
    return

  for i in range(index, len(s)):
    if not visited[i]:
      visited[i] = True
      ans.append(s[i])
      lotto(i, s, visited, ans)
      ans.pop()
      visited[i] = False
    


while True:
  a = list(map(int, sys.stdin.readline().split()))
  k = a[0]
  if k == 0:
    break
  s = a[1:]
  ans = []
  visited = [False] * k
  lotto(0, s, visited, ans)
  print()