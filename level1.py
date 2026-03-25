""" ad = input("Lütfen adınızı giriniz: ")
print(f"Merhaba {ad}!")
yas = int(input("Lütfen yaşınızı giriniz: "))
if yas < 18:
    print(f"Merhaba {yas}, maalesef ehliyet almak için yeterli yaşta değilsiniz.")
elif yas >= 18:
    print(f"Tebrikler {yas} yaşındasınız, ehliyet alabilirsiniz!")
else:
    print("Geçersiz yaş girdiniz.") """


"""Adın
Yaşın
Boyun (metre cinsinden, örn: 1.75)
Python öğreniyor musun? (True/False)"""

ad = input("Lütfen adınızı giriniz: ")
yas = int(input("Lütfen yaşınızı giriniz: "))
boy = float(input("Lütfen boyunuzu metre cinsinden giriniz: "))
python = bool(input("Python öğreniyor musunuz? (Evet/Hayır): "))
print(f"Adım: {ad}")
print(f"Yaşım: {yas}")
print(f"Boyum: {boy}")
print(f"Python öğreniyor musun?: {python}")