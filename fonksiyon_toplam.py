#Liste toplamını fonksiyonla yap
"""liste = [1,2,3,4]
def toplam(liste):
    toplam = 0
    for i in liste:
        toplam = toplam + i
    return toplam
toplam(liste)
print(toplam(liste))"""


#En büyük sayıyı bulan fonksiyon yaz
"""liste = [3,7,2,9,5]
def en_buyuk_sayi (liste):
    max_deger = liste[0]
    for i in liste:
        if i > max_deger:
            max_deger = i
    return max_deger
en_buyuk_sayi(liste)
print(en_buyuk_sayi(liste))"""


#Listeyi ters çeviren fonksiyon yaz
"""liste = [1,2,3,4]
birinci_eleman = liste[0]
ikinci_eleman = liste[1]
ucuncu_eleman = liste[2]
dorduncu_eleman = liste[3]
yeni_liste = []
def ters_liste(liste):
    for i in liste:
        if i in yeni_liste:
            yeni_liste.append(dorduncu_eleman)
        elif i in yeni_liste:
            yeni_liste.append(ucuncu_eleman)
            yeni_liste.append(ikinci_eleman)
            yeni_liste.append(birinci_eleman)
    return dorduncu_eleman, ucuncu_eleman, ikinci_eleman, birinci_eleman
print(ters_liste(liste))"""


#Tekrar edenleri kaldır
"""liste = [1, 2, 2, 3, 3, 4]
def tekrar_liste(liste):
    yeni_liste = []
    for i in liste:
        if i not in yeni_liste:
            yeni_liste.append(i)
    return yeni_liste
tekrar_liste(liste)
print(tekrar_liste(liste))"""

#En çok tekrar eden sayıyı bul (fonksiyonla)
"""liste = [1, 2, 2, 3, 3, 3, 4]
sayac = {}
for i in liste:
    if i in sayac:
        sayac[i] =sayac[i] + 1
    else:        sayac[i] = 1
def tekrar_sayisi(sayac):
    max_sayi = None
    max_adet = 0
    for i in sayac:
        if sayac[i] > max_adet:
            max_sayi = i
            max_adet = sayac[i]
    return max_sayi
tekrar_sayisi(sayac)
print(tekrar_sayisi(sayac))"""

        
