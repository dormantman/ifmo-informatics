'''
 Множества
'''
# создание множества
b1 = set()
print("Set b1 = ", b1)
b2 = {"bear", "fox", "squirrel", "woodpecker",
      "woodpecker", "wolf", "hedgehog"}
print("Set b2 = ", b2)
# создание множества из строки
b3 = set("abcdabcdefg")
print("Set b3 from string: ", set(b3))
print("\n")

s = "Electricity is the set of physical phenomena associated with the presence of electric charge. Lightning is one " \
    "of the most dramatic effects of electricity"
set1 = set(s)
print(set1)
vowels = set('AEIOUYaeiouy')
for letter in set1:
    if letter in vowels:
        print(letter, end=", ")
