#topla(3, 5)
"""def topla(a, b):
    return a + b
print(topla(3, 5))"""

""" selam_ver(isim):
    print(isim, "Merhaba")
selam_ver("Mürsel")

def selam_ver(x):
    print("Merhaba", x)

selam_ver("Mürsel")

def yazdir(programlama_dili):
    print(programlama_dili , "öğreniyorum")
yazdir("Python")

def yazdir(derleyici):
    print(derleyici, "çok güzel")
yazdir("Python")"""


"""i = int(input("Bir sayı giriniz: "))
def cift_mi(sayi):
    if sayi %2 ==0:
        print("Girdiğiniz sayı çift midir?", sayi)
    else:        
        print("Girdiğiniz sayı tek midir?", sayi)
cift_mi(sayi)"""

"""i = int(input("Bir sayı giriniz: "))
def cift_mi(sayi):
    if sayi %2 ==0:
        return True
    else:        
        return False
cift_mi(sayi)
print("Sonuç doğru mu kontrol et:", cift_mi(sayi))"""

liste = [1,2,3,4,5,6]
cift_sayilar_kumesi = []
def cift_sayilar(liste):
    for sayi in liste:
        if sayi %2 ==0:
            cift_sayilar_kumesi.append(sayi)
cift_sayilar(liste)
print("Çift sayılar:", cift_sayilar_kumesi)









