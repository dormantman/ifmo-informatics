import itertools

z = input("ВВедите строку:")
x = list()
for i in range(1, len(z) + 1):
    x = x + list(map(''.join, itertools.permutations(z, i)))
print(set(x))
