# TEK sayıları yeni listeye at
"""[1, 4, 7, 10, 13, 16]
liste = [1, 4, 7, 10, 13, 16]
yeni_liste = []
for i in liste:
    if i %2 != 0:
        yeni_liste.append(i)
print(yeni_liste)"""

#Listedeki sayıları TERS çevir

from itertools import count


[1, 4, 7, 10, 13, 16]
"""liste = [1, 4, 7, 10, 13, 16]
yeni_liste = liste[::-1]
print(yeni_liste)"""

"""liste = [1, 4, 7, 10, 13, 16]
liste.reverse()
print(liste)"""

#Listedeki tekrar eden elemanları kaldır
[1, 4, 7, 10, 13, 16]
"""liste = [1, 4, 7, 10, 13, 16, 4, 7]
yeni_liste = []
for i in liste:
    if i not in yeni_liste:
        yeni_liste.append(i)
print(yeni_liste)"""

#Listedeki en büyük ve en küçük farkını bul
[10, 3, 45, 23, 8]
"""liste = [10, 3, 45, 23, 8]
max_deger = liste[0]
for i in liste:
    if i > max_deger:
        max_deger = i
min_deger = liste[0]
for i in liste:
    if i < min_deger:
        min_deger = i
fark = max_deger - min_deger
print(fark)"""

#Listedeki sayıları iki listeye ayır
"""[1, 2, 3, 4, 5, 6]
liste = [1, 2, 3, 4, 5, 6]
tek_liste = []
çift_liste = []
for i in liste:
    if i %2 != 0:
        tek_liste.append(i)
    else:
        çift_liste.append(i)
print("Tek sayılar:", tek_liste)
print("Çift sayılar:", çift_liste)"""

#Listedeki en çok tekrar eden elemanı bul
[1, 2, 2, 3, 3, 3, 4]
liste = [1, 2, 2, 3, 3, 3, 4]
en_cok_tekrar_eden = None
en_cok_tekrar_sayisi = 0
for i in liste:
    tekrar_sayisi = liste.count(i)
    if tekrar_sayisi > en_cok_tekrar_sayisi:
        en_cok_tekrar_eden = i
        en_cok_tekrar_sayisi = tekrar_sayisi
print("En çok tekrar eden eleman:", en_cok_tekrar_eden)