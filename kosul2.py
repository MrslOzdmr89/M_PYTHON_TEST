sayi = int(input("Lütfen bir sayı giriniz: "))
if sayi == 0:
    print("Sayı sıfırdır.")
elif sayi % 2 == 0:
    print(f"{sayi} çift bir sayıdır.")
else:
    print(f"{sayi} tek bir sayıdır.")