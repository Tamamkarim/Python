sana = input("Anna merkkijono: ")
osajonot = [sana[i:] for i in range(len(sana))]  # luodaan lista kaikista osajonoista
osajonot.sort(key=len)  # järjestetään osajonot pituusjärjestykseen

for osajono in osajonot:
    print(osajono)
