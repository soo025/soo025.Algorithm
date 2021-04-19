d = [[0]*11 for _ in range(100+1)]
MOD = 1000000000
for i in range(1, 10):
  d[1][i] = 1

n = int(input())

for i in range(2, n+1) :
  for j in range(0, 10) :
    d[i][j] += (d[i-1][j-1] + d[i-1][j+1] ) % MOD

print(sum(d[n])%MOD)
