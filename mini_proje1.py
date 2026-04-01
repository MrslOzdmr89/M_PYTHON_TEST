#Cümlede kelime frekansı
cümle = "ben geliyorum ben"
kelimeler = cümle.split() # cümleyi kelimelere ayırır
print(kelimeler)
frekans_kelimeler = {}
for kelime in kelimeler:
    if kelime in frekans_kelimeler:
        frekans_kelimeler[kelime] += 1
    else:
        frekans_kelimeler[kelime] = 1
print(frekans_kelimeler)