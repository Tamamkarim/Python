def viiva(pituus):
    for i in range(pituus):
        print("#", end="")
    print()

def risulaatikko(korkeus):
    viiva(10)
    for i in range(korkeus-2):
        print("#        #")
    viiva(10)
