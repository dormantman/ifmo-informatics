'''
Списки
'''
a = [1, 2, 3, 4, 5]
print("a[0]: ", a[0])
print("List a[0:5]: ", a[0:5])
print("List a[:]: ", a[:])
print("List a: ", a)
print("List a[1:5]: ", a[1:])
print("List a[0:4]: ", a[:4])
print("Length of list a: ", len(a))
print("\nList a (by index):")
# получение слементов списка в цикле (1)
for i in range(0, len(a)):
    print(a[i], end=" ")
print("\nList a (by elements):")
# получение слементов списка в цикле (2)
for elem in a:
    print(elem, end=" ")
print("\n")
b = []
b.append(20)  # добавление слемента в конец
b.extend(a)  # добавление слементов списка a в b
print("List b (extended): ", b)
b.insert(3, 5)  # добавить слемент на позицию
print("List b (insert element): ", b)
b.remove(5)  # удалить первый слемент, равный 5
print("List b (remove element): ", b)
c1 = b.pop()  # удалить и вернуть последний слемент
print("List b (pop last element): ", b)
print("c1: ", c1)
c2 = b.pop(3)  # удалить и вернуть сл. с позиции
print("List b (pop 3rd element): ", b)
print("c2: ", c2)
bCopy = b.copy()  # создать копию списка
print("List b: ", b)
print("List bCopy: ", bCopy)
b.reverse()  # поменсть слем. местами с конца в начало
print("List b (reversed): ", b)
b.sort(reverse=True)  # сортировка слементов списка
print("List b (sorted): ", b)
b.clear()  # очистка списка
print("List b (cleared): ", b)
print("\n")
# сравнение списков
a1 = [1, 2, 4]
a2 = [1, 2, 3]
print("a1 == a2: ", a1 == a2)
a1.append(-1)
print("a1 == a2: ", a1 == a2)
print("a1 > a2: ", a1 > a2)
print("a1 < a2: ", a1 < a2)
print("\n\n")

# Задание 9
n = int(input())
list1 = list()
for i in range(n):
    list1.append(int(input()))
list1.sort(reverse=True)
print(list1[5:10])
print('\n')

# Задание 10
list2 = list1.copy()
list2.reverse()
print(list1)
print(list2)
