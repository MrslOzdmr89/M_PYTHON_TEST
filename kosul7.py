sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))
islem = input("Yapmak istediğiniz işlemi seçiniz (+, -, *, /): ")
if islem == "+":
    sonuc = sayi1 + sayi2
    print("Sonuç: ", sonuc)
elif islem == "-":
    sonuc = sayi1 - sayi2
    print("Sonuç: ", sonuc)
elif islem == "*":
    sonuc = sayi1 * sayi2
    print("Sonuç: ", sonuc)
elif islem == "/":
    sonuc = sayi1 / sayi2
    print("Sonuç: ", sonuc)