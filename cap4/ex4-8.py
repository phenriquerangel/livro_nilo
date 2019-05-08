num1=int(input("Qual numero 1? "))
num2=int(input("Qual numero 2? "))
operacao = int(input(" Qual operacao?Ex ; som, sub, mult e div  "))

if operacao == "som":
    print("Soma = %d " % num1+num2)
elif operacao == "sub":
    print("Subtração = %d " % num1-num2)
elif operacao == "mult":
    print("Multiplicação = %d" % num1*num2)
elif operacao =="div":
    print("Divisão = %d " % num1/num2)
else: 
    print(" Operação não idenfiticada!")
