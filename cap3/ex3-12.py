distance = int(input("Distance km: "))
velocity = int(input("Velocity h: "))

time=(distance/velocity)*60

print("Estimated time: %d hours" % time)