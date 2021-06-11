n = int(input())
answer = 0

for i in range(1, n+1):
  tmp = list(map(int, str(i)))
  s = i + sum(tmp)
  if s == n:
    answer = i
    break
print(answer)