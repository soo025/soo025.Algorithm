def pwd(l, a, p, index):
  
  if len(p) == l:
    if check(p):
      print(p)
      return
  if index == len(a):
    return
  pwd(l, a, p+a[index], index+1)
  pwd(l, a, p, index+1)
  
def check(p):
  mo = 0
  ja = 0
  for i in p:
    if i in 'aeiou':
      mo += 1
    else:
      ja += 1
  return mo >= 1 and ja >=2

l, c = map(int,input().split())
a = input().split()
a.sort()
pwd(l, a, "", 0)