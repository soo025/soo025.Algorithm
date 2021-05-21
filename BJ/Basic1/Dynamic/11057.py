n = int(input())
d = [1] * 10
MOD = 10007

for _ in range(n-1):
  for i in range(1, 10):
    d[i] = (d[i]+d[i-1]) % MOD
print((sum(d))%MOD)
