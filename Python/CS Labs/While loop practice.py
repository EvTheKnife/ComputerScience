n = input("Enter a number > 5: ")


while isinstance(n, int) != True or n < 5:
    try:
        n = int(n)
        if n <= 5:
            print("Number is not greater than 5")
            n = input("Enter a number > 5: ")
            continue

        if n > 5:
            break

    except:
        print("Not a valid integer")
        n = input("Enter a number > 5: ")


sequenceLetter = input("Input the letter of the sequence you want to run (A-N): ")

sequence = []

if sequenceLetter.lower() == 'a':
    startValue = 1
    sequence.append(startValue)
    for a in range(n):
        startValue += 1
        sequence.append(startValue)


if sequenceLetter.lower() == 'b':
    startValue = 2
    sequence.append(startValue)
    for b in range(n):
        startValue += 2
        sequence.append(startValue)


if sequenceLetter.lower() == 'c':
    startValue = -1
    sequence.append(startValue)
    for c in range(n):
        if startValue > 0:
            startValue += 1
            startValue *= -1
        elif startValue < 0:
            startValue *= -1
            startValue += 1
        
        sequence.append(startValue)


if sequenceLetter.lower() == "d":
    startValue = 0
    sequence.append(startValue)

    for d in range(n):
        startValue = 3 ** d
        sequence.append(startValue)






print(sequence)

        
