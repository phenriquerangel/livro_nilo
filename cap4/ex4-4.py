salario = float(input("Qual é o salario: "))
aumento = 0
dif = 0
if salario >= 1250:
    aumento=salario*1.15
    dif = aumento - salario
    print("Novo salario: %6.2f com aumento de %6.2f " % (aumento,dif))
if salario < 1250:
    aumento = salario *1.10
    dif = aumento - salario
    print("Novo salario: %6.2f com aumento de %6.2f " % (aumento,dif))