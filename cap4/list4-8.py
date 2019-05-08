category= int(input(" Digite a cagetoria do produto: "))
if category == 1:
    preco = 10
elif category == 2:
    preco = 18
elif category == 3:
    preco = 23
elif category == 4:
    preco = 26
elif category == 5:
    preco = 31
else:
    print("Categoria inválida . digite um valor entre 1 e 5!")
    preco = 0
print("O preco do produto é R$%6.2f" % preco)