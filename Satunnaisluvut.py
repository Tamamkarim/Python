import random

def arvo_luku(min_arvo, max_arvo):
    return random.randint(min_arvo, max_arvo)

def satunnaisluvut():
    ensimmainen_luku = arvo_luku(30, 100)
    luvut = []
    luvut.append(ensimmainen_luku)

    summa = ensimmainen_luku
    for _ in range(9):
        luku = arvo_luku(1, 100)
        luvut.append(luku)
        summa += luku

    keskiarvo = summa / len(luvut)

    print("Arvottujen lukujen lista:")
    print(luvut)
    print("Lukujen määrä:", len(luvut))
    print("Lukujen summa:", summa)
    print("Lukujen keskiarvo:", keskiarvo)
    
satunnaisluvut()
