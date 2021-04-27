n = int(input())
m = int(input())
if m != 0:
  a = list(input().split())
else:
  a = []

# 최대 1000000
tmp = 1000000
l = 0
ans = 0
for i in range(1000000):
  #고장난 버튼이 있으면 flag를 true로
  flag = False
  for j in str(i):
    if j in a:
      flag = True
  #flag가 true면 pass
  if flag :
    pass
  else:
    if tmp > abs(n-i):
      tmp = abs(n-i)
      l = len(str(i))
ans = min(tmp+l, abs(n-100))
print(ans)