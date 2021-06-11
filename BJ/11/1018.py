n, m = map(int, input().split())
data = []
answer = []

for _ in range(n):
  data.append(input())

# n*m 안에서
for i in range(n-7):
  for j in range(m-7):
    w = 0
    b = 0
    # 8*8 체스판
    for x in range(i, i+8):
      for y in range(j, j+8):
        # 짝수일 때
        if (x+y)%2 == 0:
          if data[x][y] != 'W':
            w += 1
          if data[x][y] != 'B':
            b += 1
        # 홀수일 때
        else:
          if data[x][y] != 'B':
            w += 1
          if data[x][y] != 'W':
            b += 1
    answer.append(w)
    answer.append(b)
print(min(answer))