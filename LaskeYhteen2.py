kieli = int(input("1 Suomi, 2 English, 3 Espangol"))
promptiLista = ["kokonaisluku: " ,"Integer: ", "Entero"]
viestiLista = ["summa on", "sum is ", "suma es "]

n1 = int(input("1. " + promptiLista[kieli-1]))
n2 = int(input("2. " + promptiLista[kieli-1]))
n3 = int(input("3. " + promptiLista[kieli-1]))
s = n1 +n2 +n3
print (viestiListaen[kieli-1] + str(s))

