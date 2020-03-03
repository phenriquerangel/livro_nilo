divida = float(input("Qual é o valor inicial da divida: "))
juros = float(input("Qual é o valor do juros mensal: "))
deposito = float(input("Qual é o valor será pago por mes: "))
mes = 1

if ( divida * (juros/100) > deposito ):
    print(" Sua divida nunca vai ser paga")
while divida > deposito:
    saldo = divida
    juros = saldo * juros /100