readd = int(input("Days: "))
readh = int(input("Hours: "))
readm = int(input("Minutes: "))
reads = int(input("Seconds: "))

#metrics
sec = 60
min = 60 
hours = 24
days = 365

#results
resultd = readd*hours*min*sec
resulth = readh*min*sec
resultm = readm*sec

_sum = resultd+resulth+resultm+reads

print("Sum equals a: %d" % _sum)