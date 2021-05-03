def leave(day, sum):
  global ans
  if day == n+1:
    ans = max(ans, sum)
    return
  if day > n+1:
    return

  leave(day+1, sum)
  leave(day+t[day], sum+p[day])


n = int(input())
t = [0] * (n+1)
p = [0] * (n+1)

for i in range(1, n+1):
  t[i], p[i] = map(int, input().split())
ans = 0
leave(1,0)
print(ans)