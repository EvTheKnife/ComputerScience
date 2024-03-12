print("Welcome to my calculator!")
x = float(input("Input your first number: "))
y = float(input("Input your second number: "))
operation = input("Input the operation: ")

if operation.lower() == "addition":
    z = x+y

if operation.lower() == "subtraction":
    z = x-y

if operation.lower() == "multiplication":
    z = x*y

if operation.lower() == "division":
    z = x/y

print(z)