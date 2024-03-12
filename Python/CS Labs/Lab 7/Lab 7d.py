spent = float(input("Enter the cost of your item: "))

if spent < 10.00:
    totalCost = spent
    print("Total cost: %6.2f" %totalCost )


if spent >= 10.00 and spent <= 50.00:
    totalCost = spent - (spent * 0.04)
    print("Total cost: $ %6.2f" %totalCost )


if spent > 50.00 and spent <=100.00:
    totalCost = spent - (spent * 0.06)
    print("Total cost: $ %6.2f" %totalCost)


if spent > 100.00 and spent <= 150.00:
    totalCost = spent - (spent * 0.08)
    print("Total cost: $ %6.2f" %totalCost)


if spent > 150.00 and spent <= 200:
    totalCost = spent - (spent * 0.10)
    print("Total cost: $ %6.2f" %totalCost)


if spent > 200.00:
    totalCost = spent - (spent * 0.12)
    print("Total cost: $ %6.2f" %totalCost)

