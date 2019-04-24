km = int(input("Km wheeled: "))
day = int(input("Days rented: "))

km_wheeled = km * 0.15
days_rented = day * 60

totalcost = km_wheeled + days_rented

print("Total cost: R$ %.2f " % totalcost)