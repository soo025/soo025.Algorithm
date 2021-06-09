def h(n, start, to, end):
  if n == 1:
    return print(start, end)
  h(n-1, start, end, to)
  print(start, end)
  h(n-1, to, start, end)

n = int(input())
print(2**n - 1)
h(n, 1, 2, 3)