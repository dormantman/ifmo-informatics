'''
 Словари
'''
d1 = {
    "day":   18,
    "month": 6,
    "year":  1983
}
d2 = dict(bananas=3, apples=5, oranges=2, bag="basket")
d3 = dict([("street", "Kronverksky pr."), ("house", 49)])
d4 = dict.fromkeys(["1", "2"], 3)
print("Dict d1 = ", d1)
print("Dict d2 by dict()= ", d2)
print("Dict d3 by dict([])= ", d3)
print("Dict d4 by fromkeys = ", d4)
print("\n")

d1 = {
    "ready": 3,
    "set":   2,
    "go":    1
}
d2 = dict(ready=3, set=2, go=1)
d3 = dict([("ready", 3), ("set", 2), ("go", 1)])

print(d1)
print(d2)
print(d3)

dict1 = dict.fromkeys(["key1", "key2"], input('value: '))
print(dict1)
