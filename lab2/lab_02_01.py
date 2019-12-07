'''
Условие
'''

# if..else
num = int(input("How many times have you been to the Hermitage? : "))
if num > 0:
    print("Wonderful!")
    print("I hope you liked this museum!")
else:
    print("You should definitely visit the Hermitage!")
# if..elif..else
course = int(input("What is your course number? : "))
if course == 1:
    print("You are just at the beginning!")
elif course == 2:
    print("You learned many things, but not all of them!")
elif course == 3:
    print("The basic course is over, it's time for professional disciplines!")
else:
    print("Oh! You need to hurry! June is the month of thesis defense")
x = 5
y = 12
if y % x > 0:
    print("%d cannot be evenly divided by %d" % (y, x))
z = 5
if y % z == 0:
    x = "{} is a divider of {}".format(z, y)
else:
    x = "{} is not a divider of {}".format(z, y)
print(x)
print("\n\n")

# Задание 2
p = int(input("Сколько Вы выполнили в стом году лабораторных работ? : "))
if p > 10:
    if p == 11:
        print("Вы выполнили в стом году " + str(p) + " лабороторных работы")
    elif (p % 10 == 4) or (p % 10 == 3) or (p % 10 == 2):
        print("Вы выполнили в стом году " + str(p) + " лабораторные работы")
    elif p % 10 == 1:
        print("Вы выполнили в стом году " + str(p) + " лабораторную работ")
    else:
        print("Вы выполнили в стом году " + str(p) + " лабораторных работ")
else:
    print("Вы не сдали зачет")
print("\n")

p = int(input())
print(p) if p > 10 else print("не сдал")
print("\n")

# Задание 3
a = 157
b = 525
if a > b:
    x = a % b
elif a:
    x = b % a
elif a == b:
    x = a * b
print(x)
