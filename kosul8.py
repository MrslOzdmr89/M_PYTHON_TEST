yas = int(input("Yaşınızı giriniz: "))
if yas < 0:
    print("Geçersiz yaş girdiniz.")
elif yas >= 0 and yas <= 12:
    print("Yaş kategoriniz: Çocuk")
elif yas >= 13 and yas <= 17:
    print("Yaş kategoriniz: Ergen")
elif yas >= 18 and yas <= 35:
    print("Yaş kategoriniz: Genç")
elif yas >= 36 and yas <= 55:
    print("Yaş kategoriniz: Yetişkin")
elif yas >= 56:
    print("Yaş kategoriniz: Yaşlı")
else:
    print("Nüfus kayıtlarına göre yaşınız tespit edilememiştir")   