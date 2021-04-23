d= [0]*(1000001)
# 공집합
d[0] = 1
MOD = 1000000009

for i in range(1, 1000001) :
  if i-1 >= 0 :
    d[i] += d[i-1]
  if i-2 >= 0 :
    d[i] += d[i-2]
  if i-3 >= 0 :
    d[i] += d[i-3]
  d[i] %= MOD
    
t = int(input())
for _ in range(t) :
  n = int(input())
  print(d[n])