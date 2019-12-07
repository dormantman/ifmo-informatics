'''
 Условие
'''

# while
print("Numbers < 10 (while):")
i = 0
while (i < 10):
    print(i, end=" ")  # print in one line
    i += 1
print("\n")

# for
print("Numbers < 10 (for):")
for i in range(0, 10):
    print(i, end=" ")
else:
    print("\nThe next number is 10\n")
# break
sum = 0
for i in range(0, 12):
    if i > 10:
        print("\nWe reached the end, final sum: ", sum)
        break
    sum += i
# continue
i = 0
while i <= 15:
    if i % 3 == 0:
        i += 1
        continue
    print(i, end=" ")
    i += 1
print("\n")
# pass
print("Let's print numbers again!")
for i in range(0, 10):
    pass
    print(i, end=" ")
print("\n\n")

i = 0
for i in range(0, 501):
    if i % 7 == 0:
        print(i, end=" ")
        i += 1
else:
    print("\nAll numbers were printed!")
print("\n")

i = 0
while (i <= 500):
    if (i % 14 == 0):
        print(i, end=" ")
    i += 1
    if i == 300:
        break
else:
    print("\nAll numbers were printed!")
print("\n")

k = 1
n = 4
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            a[i][j] = k
            k += 1
        else:
            a[i][j] = 0
for row in a:
    print(' '.join([str(elem) for elem in row]))
