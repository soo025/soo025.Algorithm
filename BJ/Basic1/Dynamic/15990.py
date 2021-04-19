MAX = 100000
MOD = 1000000009
d = [[0] * 4 for _ in range(MAX+1)]
d[1][1] = 1
d[2][2] = 1
d[3][1] = 1
d[3][2] = 1
d[3][3] = 1

for i in range(4, (MAX+1)) :
    d[i][1] = (d[i-1][2]+d[i-1][3]) % MOD
    d[i][2] = (d[i-2][1]+d[i-2][3]) % MOD
    d[i][3] = (d[i-3][1]+d[i-3][2]) % MOD

T= int(input())
for _ in range(T) :
  n = int(input())
  print(sum(d[n])%MOD)
