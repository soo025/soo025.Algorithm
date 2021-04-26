n = 9
a = [int(input()) for _ in range(n)]
# 오름차순 정렬
a.sort()
s = sum(a)
ans = []

# 9개의 합에서 가짜 난쟁이 2명의 키를 빼주면 100이 나옴
for i in range(0, n-1):
  for j in range(i+1, n):
    if (s - a[i] - a[j]) == 100:
      ans = [i, j]
      break
  if ans:
    break
    
# 가짜 난쟁이만 빼고 출력
for i in range(0, n):
  if i in ans:
    continue
  print(a[i])
