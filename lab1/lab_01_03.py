"""
Форматированный ввод/вывод данных
"""
m = 10
pi = 3.1415927
print("m =", m)
print("m = %d" % m)
print("%7d" % m)
print("pi = ", pi)
print("%.3f" % pi)
print("%10.4f\n" % pi)
print("m = {}, pi = {}".format(m, pi))
ch = 'A'
print("ch = %c" % ch)
s = "Hello"
print("s = %s" % s)
print("\n\n")

code = input("Enter your position number in group: ")
n1, n2 = input("Enter two numbers splitted by space: ").split()
d, m, y = input("Enter three numbers splitted by \'.\': ").split('.')
print("{} + {} = {}".format(n1, n2, float(n1) + float(n2)))
print("Your birthday is %s.%s.%s and you are %d in the group list" % (d, m, y, int(code)))
print('\n\n')

# Задание 16
m = 10
pi = 3.1415927
print("%4d" % m)
print("%.3f" % pi)
print("\n")

# Задание 17
print("m = {}, pi = {}".format(m, pi))
print("\n")

# Задание 18
year = input("сомер Ввашего курса: ")
print(year)
print("\n")

# Задание 19
r1, m1, p1 = input("Введите Ваши результаты ЕГЭ через запстую \',\': ").split(',')
print("Ваши результаты ЕГЭ по русскому сзыку, математике и профильному предмету: %s,%s,%s " % (r1, m1, p1,))
print('\n')

# Задание 20
x = int(input('Введите 12-ое число с основание 5:'), 5)
print(x)
print('\n')

# Задание 21
x = int(input('Введите число:'))
print("x/2=%d" % (x >> 1))
print("x*2=%d" % (x << 1))
