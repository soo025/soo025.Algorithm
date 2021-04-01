s = input()
n = int(len(s))
stack = []
ans = 0

for i in range(n) :
  if s[i] == '(' :
    stack.append(s[i])
  else :
    if s[i-1] == '(' :
      stack.pop()
      ans += len(stack)
    else :
      stack.pop()
      ans += 1
print(ans)
