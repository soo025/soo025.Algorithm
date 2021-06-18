def draw(size, x, y):
  if size == 1:
    star[x][y] = '*'
  else:
    size //= 3
    for i in range(3):
      for j in range(3):
        if i != 1 or j != 1:
          draw(size, x+(i*size), y+(j*size))


n = int(input())
star = [[' ' for _ in range(n)] for _ in range(n)]

draw(n,0,0)
for s in star:
  print(''.join(s))
