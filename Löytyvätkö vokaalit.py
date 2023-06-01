merkkijono = input("Anna merkkijono: ")
vokaalit = ['a', 'e', 'o']
for vokaali in vokaalit:
    if vokaali in merkkijono:
        print(vokaali, "löytyy")
    else:
        print(vokaali, "ei löydy")
§