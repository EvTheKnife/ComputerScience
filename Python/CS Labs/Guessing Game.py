import random as rand

lowGuessRange = 1
highGuessRange = int(input("Input the upper value that the guess should be in: "))

correctNum = rand.randint(lowGuessRange, highGuessRange)

userNum = int(input(f"Input your guess (from {lowGuessRange} to {highGuessRange}): "))

numGuesses = 1

while userNum != correctNum:

    if userNum < correctNum:
        print("Too low!")

    if userNum > correctNum:
        print("Too high!")

    userNum = int(input("Input your guess(from {lowGuessRange} to {highGuessRange}): "))

    numGuesses += 1


if userNum == correctNum:
    print(f"You guessed it in {numGuesses} guess(es)!")
    
