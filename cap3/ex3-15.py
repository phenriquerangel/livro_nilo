cigarrets = int(input("Cigarrets: "))
year = int(input("Years: "))
cig_per_day = (year*365)*cigarrets
time_left=((cig_per_day/60)/24)*10
print("Time over: %0.1f days" % time_left)