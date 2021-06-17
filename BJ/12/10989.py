import sys
n = int(sys.stdin.readline())
a = [0] * 10001

for i in range(n):
  a[(int(sys.stdin.readline()))] += 1
  
for i in range(10001):
  # 카운팅 되었을 경우
  if a[i] >= 1:
    # a[i]의 값만큼
    for j in range(a[i]):
      print(i)