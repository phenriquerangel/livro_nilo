velocidade = int(input("Qual é a velocidade do carro: "))

if velocidade <= 80:
    print("Dentro do permitido!")
if velocidade > 81:
    print("Multa de R$ 5 por estar acima de 80km/h!")
