# 값을 더한 뒤 부호를 비교
def check(index):
  sum = 0
  for i in range(index, -1, -1):
    sum += ans[i]
    if sum == 0 and a[i][index] != 0:
      return False
    elif sum > 0 and a[i][index] <= 0:
      return False
    elif sum < 0 and a[i][index] >= 0:
      return False
  return True

def go(index):
  if index == n:
    return True

  if a[index][index] == 0:
    ans[index] = 0
    return go(index+1)

  # 부호를 곱하여 경우의 수를 반으로 줄임
  for i in range(1, 11):
    ans[index] = i * a[index][index]
    if check(index) and go(index+1):
      return True
  return False

n = int(input())
s = input()
a = [[0]*n for _ in range(n)]
cnt = 0
ans = [0]*n

for i in range(n):
  for j in range(i, n):
    if s[cnt] == '0':
      a[i][j] = 0
    elif s[cnt] == '+':
      a[i][j] = 1
    else:
      a[i][j] = -1
    cnt+=1
go(0)
print(' '.join(map(str, ans)))