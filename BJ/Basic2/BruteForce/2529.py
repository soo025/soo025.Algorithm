def it(x, y, op)
  if op == ''
    if x  y
      return True

  if op == ''
    if x  y
      return True
  

def ies(index, n)
  if index == k+1
    ans.append(n)
    return

  for i in range(10)
    if check[i]
      continue
      
    if index == 0 or it(n[index-1], str(i), a[index-1])
      check[i] = True
      ies(index+1, n+str(i))
      check[i] = False
  


k = int(input())
a = input().split()
check = [False]  10
ans = []
ies(0,'')
ans.sort()
print(ans[-1])
print(ans[0])