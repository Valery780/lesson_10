m = int(input('Enter a number: '))

n = 5
a = []
for i in range(1, n + 1):
    b = i
    a.append(b)
    print("%4d" % b, end='')
print()

for j in range(abs(m)):
    if m < 0:
        for i in range(n - 1):
            a[i] = a[i + 1]
        a[n - 1] = 0
    elif m > 0:
        for i in range(n - 1, 0, -1):
            a[i] = a[i - 1]
        a[0] = 0
    for i in a:
        print("%4d" % i, end='')
    print()

