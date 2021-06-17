import sys
from collections import Counter

n = int(sys.stdin.readline())
a = []
for _ in range(n):
  a.append(int(sys.stdin.readline()))
a.sort()

# 1. 산술평균
print("%.0f"%(sum(a)/n))

# 2. 중앙값
print(a[n//2])

# 3. 최빈값
m = Counter(a).most_common()
if n > 1:
  if m[0][1] == m[1][1]:
    print(m[1][0])
  else:
    print(m[0][0])
else:
  print(m[0][0])

# 4. 범위
print(max(a) - min(a))