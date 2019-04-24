product=int(input("Product : "))
discount=int(input("Descount : "))

newprice = product-((product*discount)/100)
discount = product - newprice

print("Product with discount: %0.2d" % newprice)
print("Difference: %0.2d " % discount)

