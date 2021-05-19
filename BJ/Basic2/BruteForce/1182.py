def dfs(index, sum):
  global cnt
  if index >= n:
    return
  sum += a[index]
  if sum == s:
    cnt += 1
  dfs(index+1, sum)
  dfs(index+1, sum-a[index])

n, s = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
dfs(0, 0)
print(cnt)