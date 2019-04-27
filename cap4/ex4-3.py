a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))

if a > b and a > c:
    print("Valor: %d é o maior"  % a)
if b > a and b > c:
    print("Valor: %d é o maior"  % b)
if c > a and c > b:
    print("Valor: %d é o maior"  % c)
    
if a < b and a < c:
    print("Valor: %d é o menor"  % a)
if b < a and b < c:
    print("Valor: %d é o menor"  % b)
if c < a and c < b:
    print("Valor: %d é o menor"  % c)