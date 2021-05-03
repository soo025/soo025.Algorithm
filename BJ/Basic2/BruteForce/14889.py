def ab(index, first, second):
  if index == n:
    if len(first) != n//2 or len(second) != n//2:
      return -1

    t1 = 0
    t2 = 0
    for i in range(n//2):
      for j in range(n//2):
        t1 += s[first[i]][first[j]]
        t2 += s[second[i]][second[j]]
    d = abs(t1 - t2)
    return d

  ans = -1
  t1 = ab(index+1, first+[index], second)
  t2 = ab(index+1, first, second+[index])
  if ans == -1 or (t1 != -1 and ans > t1):
    ans = t1
  if ans == -1 or (t2 != -1 and ans > t2):
    ans = t2
  return ans

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
print(ab(0, [], []))