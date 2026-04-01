liste = ['a', 'a', 'b', 'b', 'b', 'b', 'b', 'c', 'c', 'c']
dict3 = {}
for i in liste:
    if i in dict3:
        dict3[i] = dict3[i] + 1
    else:
        dict3[i] = 1
print(dict3)
print(dict3.keys())
print(dict3.values())
print(dict3.items())

# anahtarlar
for k in dict3.keys():
    print(k, end=" ")
print()

# değerler
for v in dict3.values():
    print(v, end=" ")
print()

# anahtar + değer
for k, v in dict3.items():
    print(k, v)