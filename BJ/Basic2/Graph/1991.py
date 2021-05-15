class Node:
  def __init__(self, left, right):
    self.left = left
    self.right = right

d = dict()
A = ord('A')

# 전위순회
def preoder(x):
  if x == -1:
    return
  print(chr(A+x), end = '')
  preoder(d[x].left)
  preoder(d[x].right)

# 중위순회
def inoder(x):
  if x == -1:
    return
  inoder(d[x].left)
  print(chr(A+x), end = '')
  inoder(d[x].right)

# 후위순회
def postoder(x):
  if x == -1:
    return
  postoder(d[x].left)
  postoder(d[x].right)
  print(chr(A+x), end = '')

n = int(input())
for _ in range(n):
  x, y, z = input().split()
  x = ord(x) - A

  # 이진노드 숫자로
  if y == '.':
    y = -1
  else:
    y = ord(y) - A

  if z == '.':
    z = -1
  else:
    z = ord(z) - A
    
  # 노드 추가
  d[x] = Node(y, z)

preoder(0)
print()
inoder(0)
print()
postoder(0)
print()