wage = float(input())
hoursWorked = float(input())

if hoursWorked < 1:
    print("404: HOURS NOT FOUND")

if hoursWorked <= 40:
    print(wage * hoursWorked)

if hoursWorked > 40:
    print((wage *40) + ((hoursWorked - 40) * (1.5 * wage)))
