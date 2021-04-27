t = int(input())
for _ in range(t):
  M, N, x, y = map(int, input().split())
  k = x
  while k < M*N:
    if (k-y) % N == 0:
      print(k)
    k += M
  else:
    print(-1)
    