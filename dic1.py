"""[1, 2, 2, 3, 3, 3, 4]
dict1 = {}
for i in [1, 2, 2, 3, 3, 3, 4]:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
print(dict1)"""


#Dictionary’den en çok tekrar eden sayıyı bul
numbers = [1, 2, 2, 3, 3, 3, 4]
max_sayi = None
max_adet = 0
dict1 = {}
for i in numbers:
    if i in dict1:
        dict1[i] = dict1[i] + 1
    else:
        dict1[i] = 1
print(dict1)
for i in numbers:
    tekrar_sayisi = dict1[i]
    if tekrar_sayisi > max_adet:
        max_sayi = i
        max_adet = tekrar_sayisi
print("En çok tekrar eden sayı:", max_sayi)






