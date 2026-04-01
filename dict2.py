#Kullanıcıdan kelime al → harf frekansı çıkar
"""kelime = input("Bir kelime giriniz: ")
harf_frekansi = {}
for harf in kelime:
    if harf in harf_frekansi:
        harf_frekansi[harf] += 1
    else:
        harf_frekansi[harf] = 1
print(harf_frekansi)"""


#En çok geçen harfi bul
"""kelime = input("Bir kelime giriniz: ")
harf_frekansi = {}
max_harf = None
max_sayi = 0
for harf in kelime:
    if harf in harf_frekansi:
        harf_frekansi[harf] += 1
    else:
        harf_frekansi[harf] = 1
print(harf_frekansi)
for harf in kelime:
    tekrar_sayisi = harf_frekansi[harf]
    if tekrar_sayisi > max_sayi:
        max_harf = harf
        max_sayi = tekrar_sayisi
print("En çok geçen harf:", max_harf)
print("Frekansı:", max_sayi)"""


#Dictionary’yi ters çevir
"""kelime = input("Bir kelime giriniz: ").lower()
dict2 = {}
for harf in kelime:
    if harf in dict2:
        dict2[harf] += 1
    else:
        dict2[harf] = 1
yeni_dict = {}                                                                 
for harf in dict2:
    yeni_dict[dict2[harf]] = harf
print(yeni_dict)"""

#Doğrusu:
"""yeni_dict = {}

for harf in dict2:
    deger = dict2[harf]

    if deger in yeni_dict:
        yeni_dict[deger].append(harf)
    else:
        yeni_dict[deger] = [harf]

print(yeni_dict)"""


kelime = input("Bir kelime giriniz: ")
harf_frekansi = {}
max_harf = None
max_sayi = 0
for harf in kelime:
    if harf in harf_frekansi:
        harf_frekansi[harf] += 1
    else:
        harf_frekansi[harf] = 1
print(harf_frekansi)
for harf in kelime:
    tekrar_sayisi = harf_frekansi[harf]
    if tekrar_sayisi > max_sayi:
        max_harf = harf
        max_sayi = tekrar_sayisi
print("En çok tekrar eden harfler")
for harf in harf_frekansi:
    if harf_frekansi[harf] == max_sayi:
        print(harf)

