km = int(input("Digite a distancia: "))
passagem = 0 
if km <= 200:
    passagem = km*0.50
    print("A passagem custa: R$ %3.2f" % passagem)
else:
    passagem = km*0.45
    print("A passagem custa: R$ %3.2f" % passagem)