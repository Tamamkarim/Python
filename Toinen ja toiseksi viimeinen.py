sana = input("Anna sana: ")

if len(sana) < 2:
    print("Sana on liian lyhyt.")
else:
    if sana[1] == sana[-2]:
        print(f"Toinen ja toiseksi viimeinen kirjain on {sana[1]} ")
    else:
        print("Toinen ja toiseksi viimeinen kirjain eroavat")