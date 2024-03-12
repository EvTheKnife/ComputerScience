mass = float(input("Input teh mass (in kg)"))
rotSpeed = float(input("Input teh rotation sped"))
length = float(input("Input teh length of da rop"))

tension = mass * rotSpeed**2 / length

if tension >= 60:
    print("Da rop shall break.")

else:
    print("Da rop shant break.")