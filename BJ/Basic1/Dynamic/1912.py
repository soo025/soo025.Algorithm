n = int(input())
a = list(map(int, input().split()))
d = [0] * n

for i in range(n) :
  if a[i] < a[i] + d[i-1] :
    d[i] = a[i] + d[i-1]
  else :
    d[i] = a[i]
print(max(d))