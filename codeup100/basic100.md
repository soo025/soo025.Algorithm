# 1. 진수

## 6027

[6024](https://codeup.kr/problem.php?id=6027)

> 풀이

```python
a = int(input())
print('%x'% a)
```



## 6028

[6028](https://codeup.kr/problem.php?id=6028)

> 풀이

```python
a = int(input())
print('%X'% a)
```


## 6029

[6029](https://codeup.kr/problem.php?id=6029)

>풀이

```python
a = int(input(), 16)
print('%o'% a)
```


## 6030

[6030](https://codeup.kr/problem.php?id=6030)

>풀이

```python
n = ord(input())
print(n)
```



## 6031

[6031](https://codeup.kr/problem.php?id=6031)

>풀이

```python
c = int(input())
print(chr(c))
```


---


# 2. 3항 연산


## 6064

[6064](https://codeup.kr/problem.php?id=6064)

> 풀이

```python
a, b, c= map(int, input().split())
print((a if a<b else b) if ((a if a<b else b)<c) else c)
```


---


# 3. 종합

## 6079

[6079](https://codeup.kr/problem.php?id=6079)

> 풀이

```python
import sys

n = int(sys.stdin.readline())
r = 0
for i in range(n) :
  if r >= n :
    print(i-1)
    break
  r += i
```



## 6081


[6081](https://codeup.kr/problem.php?id=6081)

>풀이

```python
n = int(input(), 16)

for i in range (1, 16) :
  print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')
```



## 6082

[6082](https://codeup.kr/problem.php?id=6082)

>풀이

```python
n = int(input())
for i in range(1, n+1) :
  if (i%10==3 or i%10==6 or i%10==9) :
    print("X", end=' ')
  else :
    print(i, end=' ')
```



---


# 4. 리스트

## 6092

[6092](https://codeup.kr/problem.php?id=6092)

> 풀이

```python
import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
d = [0 for i in range(24)]
for i in range(n) :
    d[a[i]] += 1
    
for i in range(1,24) :
    print(d[i], end=' ')
```


## 6095

[6095](https://codeup.kr/problem.php?id=6095)

> 풀이

```python
import sys
d = [[0 for j in range(20)] for i in range(20)]

n = int(sys.stdin.readline())
for i in range(n) :
  x, y = map(int, sys.stdin.readline().split())
  d[x][y] = 1

for i in range(1, 20) :
  for j in range(1, 20) :
    print(d[i][j], end= ' ')
  print()
```



## 6096

[6096](https://codeup.kr/problem.php?id=6096)


> 풀이

```python
import sys

d = [[0 for j in range(20)] for i in range(20)]

for i in range(19) :
  inputd = list(map(int, sys.stdin.readline().split()))
  for j in range(19) :
    d[i+1][j+1] = inputd[j]

n = int(input())

for i in range(n) :
  x, y = map(int, sys.stdin.readline().split())
  for j in range(1, 20) :
    if d[x][j] == 0 :
      d[x][j] = 1
    else :
      d[x][j] = 0
      
    if d[j][y] == 0 :
      d[j][y] = 1
    else :
      d[j][y] = 0

for i in range(1, 20) :
  for j in range(1, 20) :
    print(d[i][j], end=' ')
  print()
```


## 6097

[6097](https://codeup.kr/problem.php?id=6097)

>풀이

```python
import sys


h, w = map(int, sys.stdin.readline().split())

b = [[0 for i in range(w+1)] for j in range(h+1)]

n = int(input())

for i in range(n) :
  l, d, x, y = map(int, sys.stdin.readline().split())
  for j in range(l) :
    if d == 0 :
      b[x][y+ j] = 1
    else :
      b[x+j][y] = 1

for i in range(h) :
  for j in range(w) :
    print(b[i+1][j+1], end=' ')
  print()

```


## 6098

[6098](https://codeup.kr/problem.php?id=6098)

>풀이

```python
import sys

b =[[0 for i in range(11)]for j in range(11)]

for i in range(10) :
  inputb = list(map(int, sys.stdin.readline().split()))
  for j in range(10) :
    b[i+1][j+1] = inputb[j]

x = 2
y = 2
b[x][y] = 9

  
while True :
  if b[x][y+1] == 0 :
    y += 1
    b[x][y]=9
  elif b[x][y+1] == 1 :
    if b[x+1][y] == 1 :
      break
    elif b[x+1][y] == 2 :
      x += 1
      b[x][y] =9
      break
    else :
      x += 1
      b[x][y] = 9
  else :
    y +=1
    b[x][y] = 9
    break

for i in range(1,11) :
  for j in range(1, 11) :
    print(b[i][j], end=' ')
  print()
```
