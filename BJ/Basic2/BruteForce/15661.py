def ab(index, first, second):
  if index == n:
    if len(first) == 0 or len(second) == 0:
      return -1
    t1 = 0
    t2 = 0
    for i in first:
      for j in first:
        if i == j:
          pass
        t1 += s[i][j]
    for i in second:
      for j in second:
        if i == j:
          pass
        t2 += s[i][j]
    d = abs(t1 - t2)
    return d
    
  ans = -1
  t1 = ab(index+1, first+[index], second)
  t2 = ab(index+1, first, second+[index])
  if ans == -1 or (t1 < ans and t1 != -1):
    ans = t1
  if ans == -1 or (t2 < ans and t2 != -1):
    ans = t2
  return ans


n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
print(ab(0,[],[]))