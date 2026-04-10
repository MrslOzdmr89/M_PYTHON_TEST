#chatbot tek seferlik konuşuyor
"""mesaj = input("Merhaba! Ben bir chatbot'um. Size nasıl yardımcı olabilirim? ")

if mesaj.lower() == "merhaba":
    print("Merhaba!")

elif mesaj.lower() == "nasılsın":
    print("İyiyim, sen nasılsın?")

else:
    print("Anlamadım")"""


#şimdi sürekli konuşan chatbot yapıyoruz

"""print("Merhaba! Ben bir chatbot'um Size nasıl yardımcı olabilirim? Çıkmak için 'çık' yazabilirsiniz.")

while True:
    mesaj = input("Sen: ")

    if mesaj.lower() == "merhaba":
        print("Bot: Merhaba!")

    elif mesaj.lower() == "nasılsın":
        print("Bot: İyiyim, sen nasılsın?")

    elif mesaj.lower() == "çık":
        print("Bot: Görüşürüz!")
        break

    else:
        print("Bot: Anlamadım")"""

#şimdi de chatbot'a hafıza ekleyelim.
"""isim = None

print("Merhaba! Ben bir chatbot'um.")

while True:
    mesaj = input("Sen: ")

    if mesaj.lower() == "çık":
        print("Bot: Görüşürüz!")
        break

    elif mesaj.lower() == "merhaba":
        print("Bot: Merhaba, ismin nedir?")
        isim = input("Sen: ")
        print(f"Bot: Merhaba {isim}!")

    elif mesaj.lower() == "nasılsın":
        if isim:
            print(f"Bot: İyiyim {isim}!")
        else:
            print("Bot: İyiyim!")

    else:
        print("Bot: Anlamadım")"""


#şimdi de chatbot'a daha fazla özellik ekleyelim.

isim = None
print("Merhaba! Ben bir chatbot'um.")

while True:
    mesaj =input("Sen:")
    if mesaj.lower() == "çık":
        print("Bot: Görüşürüz!")
        break
    
    elif mesaj.lower() == "merhaba":
        print("Bot: Merhaba, ismin nedir?")
        isim = input("Sen: ")
        print(f"Bot: Merhaba {isim}!")

    elif mesaj.lower() == "nasılsın":
        if isim:
            print(f"Bot: İyiyim {isim}!")
        else:
            print("Bot: İyiyim!")
    
    elif mesaj.lower() == "Adım ne?":
        if isim:
            print(f"Bot: Senin adın {isim}!")
        else:
            print("Bot: Adını bilmiyorum.")
    else:    
        print("Bot: Anlamadım")

        
    

