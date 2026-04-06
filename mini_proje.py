liste = [int(i) for i in input("Lütfen aralarda boşluk bırakarak sayı listesi giriniz: ").split()]
def ayir(liste):
    cift = []
    tek = []
    for i in liste:
        if i % 2 == 0:
            cift.append(i)
        else:
            tek.append(i)
    return cift, tek

cift, tek = ayir(liste)

print("Çift sayılar:", cift)
print("Tek sayılar:", tek)

toplam = sum(cift) + sum(tek)
print("Toplam:", toplam)


