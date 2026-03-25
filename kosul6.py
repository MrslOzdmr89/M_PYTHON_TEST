sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))
sayi3 = int(input("Üçüncü sayıyı giriniz: "))
if (sayi1 > sayi2) and (sayi1 > sayi3):
    print("En büyük sayı: ", sayi1)
elif (sayi2 > sayi1) and (sayi2 > sayi3):
    print("En büyük sayı: ", sayi2)
elif sayi1 == sayi2 == sayi3:
    print("Tüm sayılar eşittir.")
else:
    print("En büyük sayı: ", sayi3)