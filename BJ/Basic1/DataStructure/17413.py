s = input()
tag = False
stack = []

for ch in s :
  if ch == '<' :
    tag = True
    print(''.join(stack[::-1]), end='')
    stack.clear()
    print(ch, end='')
  elif ch == '>' :
    tag = False
    print(ch, end='')
  elif tag :
    print(ch, end='')
  else :
    if ch == ' ' :
      print(''.join(stack[::-1]), end='')
      stack.clear()
      print(ch, end='')
    else :
      stack.append(ch)
print(''.join(stack[::-1]), end='\n')
