sana = input("Sana: ")
pituus = len(sana)
taytto = 28 - pituus
vasen_taytto = taytto // 2
oikea_taytto = taytto - vasen_taytto
#if pituus % 2 == 0:
    #vasen_taytto -= 1
#    oikea_taytto -= 1

ylaraja = '*' * 30
alaraja = ylaraja
keskirivi = '*' + ' ' * vasen_taytto + sana + ' ' * oikea_taytto + '*'
print(ylaraja)
print(keskirivi)
print(alaraja)
