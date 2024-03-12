import random

lowGuessRange = 1
highGuessRange = int(input("Input a number that you want the range to go to! (such as 10, 50, 100) "))
print("Think of a number between 1 and", highGuessRange)

guess = highGuessRange/2
print(guess)
answerInput = ("")

while answerInput.lower() != "correct":
    if answerInput.lower() != "correct":
        answerInput = input("Say whether the number is too high too low, or correct! ")
        if answerInput.lower() == "low":
            lowGuessRange = guess+1
            guess = random.randint(int(lowGuessRange), int(highGuessRange))
            print(guess)

        if answerInput.lower() == "high":
            highGuessRange = guess-1
            guess = random.randint(int(lowGuessRange), int(highGuessRange))
            print(guess)
        else: pass

print("Yay! I guessed it!")