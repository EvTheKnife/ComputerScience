numItems = int(input("How many items? "))

price = 0.00

if input("Is this international or domestic shipping? (I, D) ") == "d":
    if input("Is this first class package or first class mail? (PKG, M) ").lower() == "pkg":
        if input("Is this retail or commercial pricing? (R, C) ").lower() == "r":
            price == 4.00
        else:
            price == 3.01

    else:
        if input("Commercial pricing or post office pricing? (C, PO) ").lower() == "po":
            price = 0.04
        else:
            price = 0.55
else:
    if input("Is this a letter or a large envelope? (L, LE) ") == "l":
        price = 1.20

    else:
        price = 2.40

total = numItems * price

print("$%-5.2f" %total)



