sayi = int(input("Lütfen bir sayı giriniz: "))
if sayi == 0:
    print("Sayı sıfırdır.")
elif sayi < 0:
    print(f"{sayi} negatif bir sayıdır.")
else:
    print(f"{sayi} pozitif bir sayıdır.")