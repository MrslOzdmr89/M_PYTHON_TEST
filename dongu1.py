"""sayac = 0
for i in range(0, 10):
    sayac += 1
    print(sayac)"""

"""for i in range(0, 100):
    if i % 2 == 0:
        print(i)"""

"""toplam = 0
i = 0
for i in range(1,101):
    toplam = toplam + i
print(toplam)"""

# print(sum(range(1, 101)))  en kısa yöntemi#


"""toplam = 0
i = 0
for i in range(1,101):
    if i % 3 == 0:
        toplam = toplam + i
print(toplam)"""



"""sayi = int(input("Sayı giriniz: "))
for i in range(1, sayi + 1):
    toplam = sayi*(sayi + 1)//2
print("Toplam: ", toplam)"""

"""sayi = int(input("Sayı giriniz: "))

toplam = 0

for i in range(1, sayi + 1):
    toplam = toplam + i
print("Toplam: ", toplam)"""


"""toplam = 0
i = 0
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        toplam = toplam + i
print(toplam)"""


"""sayi = int(input("Sayı giriniz: "))
for i in range(1, sayi + 1):
    if i % 2 == 1:
        print(i)"""


"""sayi = int(input("Sayı giriniz: "))
carpim = 1
for i in range(1, sayi + 1):
    carpim = carpim * i
print("Çarpım: ", carpim)"""


sayi = int(input("Sayı giriniz: "))
adet = 0
for i in range(1, sayi + 1):
    if sayi % i == 0:
        adet = adet + 1
        print(i)
print("Bölenlerin adedi: ", adet)

