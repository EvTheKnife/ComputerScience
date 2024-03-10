import random

fairDie_1 = random.randint(1,6)
fairDie_2 = random.randint(1,6)

numTosses = 1

sum = fairDie_1 + fairDie_2

print(f"{fairDie_1}, {fairDie_2} ({fairDie_1 + fairDie_2})")
print("Added the rolls together to generate sum")

while sum < 21:
    fairDie_1 = random.randint(1,6)
    fairDie_2 = random.randint(1,6)
    numTosses += 1
    sumThisRoll = fairDie_1 + fairDie_2
    print(f"{fairDie_1}, {fairDie_2} ({sumThisRoll}) ")
    if sumThisRoll % 2 == 0:
        sum = sum + sumThisRoll
        print("Added to sum, giving", sum)
    elif sumThisRoll < 6:
        sum = sum + 2 * sumThisRoll
        print("Multiplied by 2 and added to sum, giving", sum)
    else:
        sum = sum - sumThisRoll
        print("Subtracted from sum, giving", sum)

print(f"The final sum was {sum}")
print(f"The number of tosses it took was {numTosses}")