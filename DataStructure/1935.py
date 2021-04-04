n = int(input())
ps = input()
operand = [int(input()) for _ in range(n)]
s = []

for ch in ps :
  if ch.isupper() :
    s.append(operand[ord(ch)-ord('A')])
  else :
     b = s.pop()
     a = s.pop()
     if ch=='+': 
        s.append(a+b)
     elif ch=='-': 
        s.append(a-b)
     elif ch=='*': 
        s.append(a*b)
     elif ch=='/': 
        s.append(a/b)  
print('%.2f'%s[-1])
