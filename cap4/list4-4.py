salario=float(input(" Digite o salario para calcular o importo: "))

base = salario
imposto = 0
if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)

print("Salario R$%6.2f Imposto a pagar : R$%6.2f"% (salario,imposto))