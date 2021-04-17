import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
s = []
ans = [-1 for _ in range(n)]

for i in range(n) :
  while s and a[i] > a[s[-1]] :
    ans[s.pop()] = a[i]    
  s.append(i)
print(' '.join(map(str,ans)))
