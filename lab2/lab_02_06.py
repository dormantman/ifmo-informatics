z = input()
z = int(z, 16)

if z >= 0:
    a = bin(z)
    print(a.replace('ob', '0'))
else:
    a = list(bin(-z))
    for i in range(0, len(a)):
        if a[i] == '0':
            a[i] = '1'
    c = int(''.join(a)) + 1
    print(bin(c))
