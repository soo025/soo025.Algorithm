from itertools import combinations
n, m = map(int, input().split())
a = list(map(int, input().split()))
tmp = 0
answer = 0

for combination in list(combinations(a, 3)):
  tmp = sum(combination)
  if tmp <= m:
    answer = max(answer, tmp)

print(answer)
