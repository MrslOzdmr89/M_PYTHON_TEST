kullanici_adi = input("Lütfen kullanıcı adınızı giriniz: ")
sifre = input("Lütfen şifrenizi giriniz: ")
if kullanici_adi == "admin" and sifre == "1234":
    print("Giriş başarılı!")
elif kullanici_adi == "admin" and sifre != 1234:
    print("Kullanıcı adı veya şifre yanlış!")
elif kullanici_adi != "admin" and sifre == 1234:
    print("Kullanıcı adı veya şifre yanlış!")
else:
    print("Kullanıcı adı veya şifre yanlış!")