n = int(input())
MOD = 9901
d = [[0,0,0] for _ in range(n+1)]
d[0][0] = 1

for i in range(1, n+1):
  d[i][0] = (d[i-1][0] + d[i-1][1] + d[i-1][2]) % MOD
  d[i][1] = (d[i-1][0] + d[i-1][2]) % MOD
  d[i][2] = (d[i-1][0] + d[i-1][1]) % MOD
print(sum(d[n])%MOD)