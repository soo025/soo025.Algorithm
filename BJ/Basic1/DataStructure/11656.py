s = input()
n = len(s)
a = [s[i:] for i in range(n)]
a.sort()
print('\n'.join(a))
