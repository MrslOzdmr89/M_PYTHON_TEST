kelime = input("Bir kelime giriniz: ")
dict3 = {}
for harf in kelime:
    if harf in dict3:
        dict3[harf] += 1
    else:
        dict3[harf] = 1
print(dict3)
yeni_dict = {}
for harf in dict3:
    deger = dict3[harf]
    if deger in yeni_dict:
        yeni_dict[deger].append(harf)
    else:
        yeni_dict[deger] = [harf]
print(yeni_dict)