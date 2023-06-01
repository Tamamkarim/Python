
sana = input("Anna merkkijono: ")
viimeinen_merkki = sana[-1]
osajonot = []

# Käydään läpi kaikki mahdolliset osajonot
for i in range(len(sana)):
    for j in range(i+1, len(sana)+1):
        osajono = sana[i:j]
        if osajono[-1] == viimeinen_merkki:
            osajonot.append(osajono)

# Tulostetaan osajonot pituusjärjestyksessä
for osajono in sorted(osajonot, key=len):
    print(osajono)
