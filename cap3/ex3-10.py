salary=int(input("Salary : "))
increase=int(input("Increase : "))

newsalary = salary+((salary*increase)/100)
difference = newsalary - salary

print("New Salary: %d" % newsalary)
print("Difference: %d" % difference)

