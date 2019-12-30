n = int(input())
s = 0
if n <= 0:
    i = 1
    while i >= n:
        s += i
        i -= 1
else:
    i = 1
    while i <= n:
        s += i
        i += 1

print(s)
