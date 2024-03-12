#Chell Jorgensen

monthNum = int(input("Enter the number of the month!"))

if monthNum <= 2 or monthNum == 12:
    print("Winter")

if monthNum in range (3,5):
    print("Spring")

if monthNum in range(6,8):
    print("Summer")

if monthNum in range(9,11):
    print("Fall")