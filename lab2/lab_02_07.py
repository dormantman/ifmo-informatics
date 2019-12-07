x = input()
c = int(x, 12)
a = ''

while c > 0:
    if c % 14 == 13:
        a = a + 'D'
    elif c % 14 == 12:
        a = a + 'C'
    elif c % 14 == 11:
        a = a + 'B'
    elif c % 14 == 10:
        a = a + 'A'
    else:
        a = a + str(c % 14)
    c = (c // 14)

print(a[:: -1])
