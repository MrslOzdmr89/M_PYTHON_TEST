[1, 2, 2, 3, 3, 3, 4]
dict1 = {}
for i in [1, 2, 2, 3, 3, 3, 4]:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
print(dict1)



