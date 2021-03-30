## 6083

[6083](https://codeup.kr/problem.php?id=6083)

```python
import sys

r, g, b = map(int, sys.stdin.readline().split())

for i in range(r) :
  for j in range(g) :
    for k in range(b) :
      print(i, j, k)
print(r*g*b)
```

- 시간초과
