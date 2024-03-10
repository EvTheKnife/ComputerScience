import random

colorList = ["Red", "Blue", "Yellow", "Green", "Black", "White"]
secretList = []
def secretListGen():
    for i in range(4):
        secretList.append(colorList[random.randint(0,5)])

    print(secretList)

def inputListGen():
    isValid_1 = False
    isValid_2 = False
    isValid_3 = False
    isValid_4 = False
    isCorrect = "N"


    while isCorrect.lower() != "y":
        while isValid_1 == False:
            inputColor1 = input("Input a color from this list (as a number): (1 = red, 2 = blue, 3 = yellow, 4 = green, 5 = black, and 6 = white) ")
            try:
                inputColor1 = colorList[int(inputColor1) - 1] 
                isValid_1 = True

            except: 
                isValid_1 = False
                print("Please try inputting the color again")
        
        
        while isValid_2 == False:
            inputColor2 = input("Input a color from this list (as a number): (1 = red, 2 = blue, 3 = yellow, 4 = green, 5 = black, and 6 = white) ")
            try:
                inputColor2 = colorList[int(inputColor2) - 1] 
                isValid_2 = True

            except: 
                isValid_2 = False
                print("Please try inputting the color again")

        while isValid_3 == False:
            inputColor3 = input("Input a color from this list (as a number): (1 = red, 2 = blue, 3 = yellow, 4 = green, 5 = black, and 6 = white) ")
            try:
                inputColor3 = colorList[int(inputColor3) - 1] 
                isValid_3 = True

            except: 
                isValid_3 = False
                print("Please try inputting the color again")

        while isValid_4 == False:
            inputColor4 = input("Input a color from this list (as a number): (1 = red, 2 = blue, 3 = yellow, 4 = green, 5 = black, and 6 = white) ")
            try:
                inputColor4 = colorList[int(inputColor4) - 1] 
                isValid_4 = True

            except: 
                isValid_4 = False
                print("Please try inputting the color again")

        isCorrect = input(f"Is {inputColor1}, {inputColor2}, {inputColor3}, {inputColor4} correct? (Y, N) ")



    global userList
    
    userList = [inputColor1, inputColor2, inputColor3, inputColor4]
    #print(userList)

def guessAnswers(secretList, userList):
    
    moddedSecretList = secretList
    
    global correctSpot
    global correctColor

    correctSpot = 0
    correctColor = 0

    def findSpot():
        global correctSpot
        if moddedSecretList[0] == userList[0]:
            correctSpot += 1
            moddedSecretList[0] = "spot"

        if moddedSecretList[1] == userList[1]:
            correctSpot += 1
            moddedSecretList[1] = "spot"

        if moddedSecretList[2] == userList[2]:
            correctSpot += 1
            moddedSecretList[2] = "spot"

        if moddedSecretList[3] == userList[3]:
            correctSpot += 1
            moddedSecretList[3] = "spot"




    def findColor(correct, spot1, spot2, spot3):
        global correctSpot
        global correctColor

        if moddedSecretList[spot1] == userList[correct]:
            correctColor += 1
            moddedSecretList[spot1] = "color"

        elif moddedSecretList[spot2] == userList[correct]:
            correctColor += 1
            moddedSecretList[spot2] = "color"

        elif moddedSecretList[spot3] == userList[correct]:
            correctColor += 1
            moddedSecretList[spot3] = "color"

    findSpot()
    findColor(0, 1, 2, 3)
    findColor(1, 0, 2, 3)
    findColor(2, 0, 1, 3)
    findColor(3, 0, 1, 2)

    print(f"You have {correctSpot} color(s) in the correct spot(s) and {correctColor} with the correct color but in the wrong spot(s)")


correctSpot = 0
i = 0

while correctSpot < 4 and i != 11:
    inputListGen()
    guessAnswers(secretList, userList)

    i += 1

if correctSpot >= 4:
    print("You won! Congrats!")

if correctSpot < 4 and i == 11:
    print("You lost! :(")
