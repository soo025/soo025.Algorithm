n = int(input())
word = []
for _ in range(n):
  word.append(input())
A = ord('A')
alp = [0 for _ in range(26)]

# alp에 가중치 기록
for w in word:
  k = len(w)-1
  for c in w:
    alp[ord(c) - A] += 10 ** k
    k -= 1

# 순서대로 9부터 곱해줌
alp.sort(reverse = True)

ans = 0
for i in range(9, 0 , -1):
  ans += i * alp[9-i]
print(ans)