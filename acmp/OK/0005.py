n = int(input())
a = [int(b) for b in input().split()]
e, o = [], []
for i in range(n):
    if a[i] % 2 == 0:
        e.append(a[i])
    else:
        o.append(a[i])
for i in range(len(o)):
    print(o[i], end=' ')
print()
for i in range(len(e)):
    print(e[i], end=' ')
print()
if len(e) >= len(o):
    print('YES')
else:
    print('NO')
