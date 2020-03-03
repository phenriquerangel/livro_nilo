deposito = float(input("Qual é o valor inicial: "))
taxa = float(input("Qual é o valor da taxa (Ex.: 3 para 3%): "))
mes = 1
saldo = deposito

while mes <= 25 :
    saldo = saldo + (saldo * (taxa / 100))
    print(f"Saldo do mês {mes} é de R${saldo:5.2f}.")
    mes = mes + 1
print(f" O ganho obitido com o juros foi de R${saldo-deposito:8.2f}.")