import random 

colorList = ["black", "yellow", "red", "green", "blue", "white"]

print("Welcome to Mastermind! ")
print("I will generate 4 random colors in random positions, and you have to guess which is where! ")

secretColorList = []
for i in range(4):
    secretColorNum = random.randint(0,5)
    secretColor = colorList[secretColorNum]
    secretColorList.append(secretColor)

print(secretColorList)
blackNum = secretColorList.count("black")
yellowNum = secretColorList.count("yellow")
redNum = secretColorList.count("red")
greenNum = secretColorList.count("green")
blueNum = secretColorList.count("blue")
whiteNum = secretColorList.count("white")




def colorSetBool(colorInput, indexNum, colorNum):
    global blackNum
    global yellowNum
    global redNum
    global greenNum
    global blueNum
    global whiteNum
    global correctColor
    global correctSpot
    

    if (colorInput == "black" and blackNum != 0):
        if (colorInput == secretColorList[indexNum]):
            colorNum = True
            correctSpot = correctSpot + 1
        else:
            colorNum = False
    
    if (colorInput == "yellow" and yellowNum != 0):
        yellowNum = yellowNum - 1
        if (colorInput == secretColorList[indexNum]):
            colorNum = True
            correctSpot = correctSpot + 1
        else:
            colorNum = False
    
    if (colorInput == "red" and redNum != 0):
        redNum = redNum - 1
        if (colorInput == secretColorList[indexNum]):
            colorNum = True
            correctSpot = correctSpot + 1
        else:
            colorNum = False
    if (colorInput == "green" and greenNum != 0):
        greenNum = greenNum - 1
        if (colorInput == secretColorList[indexNum]):
            colorNum = True
            correctSpot = correctSpot + 1
        else:
            colorNum = False
    if (colorInput == "blue" and blueNum != 0):
        blueNum = blueNum - 1
        if (colorInput == secretColorList[indexNum]):
            colorNum = True
            correctSpot = correctSpot + 1
        else:
            colorNum = False
    if (colorInput == "white" and whiteNum != 0):
        whiteNum = whiteNum - 1
        if (colorInput == secretColorList[indexNum]):
            colorNum = True
            correctSpot = correctSpot + 1
        else:
            colorNum = False

def colorSweep(color1, color2, color3, color4):
    if (color1 != True):
        if (color2 == False):
            pass


for guess in range(12):
    
    blackNum = secretColorList.count("black")
    yellowNum = secretColorList.count("yellow")
    redNum = secretColorList.count("red")
    greenNum = secretColorList.count("green")
    blueNum = secretColorList.count("blue")
    whiteNum = secretColorList.count("white")

    print("Valid colors are: \"black\", \"yellow\", \"red\", \"green\", \"blue\", and \"white\"" )
    colorInput1 = input("Please input your first color: ").lower()
    colorInput2 = input("Please input your second color: ").lower()
    colorInput3 = input("Please input your third color: ").lower()
    colorInput4 = input("Please input your forth color: ").lower()
    
    userGuessList = [colorInput1, colorInput2, colorInput3, colorInput4]
    correctSpot = 0
    correctColor = 0
    if (colorInput1 in secretColorList):
        colorSetBool(colorInput1, 0, color1)
    if (colorInput2 in secretColorList):
        colorSetBool(colorInput2, 1, color2)
    if (colorInput3 in secretColorList):
        colorSetBool(colorInput3, 2 color3)
    if (colorInput4 in secretColorList):
        colorSetBool(colorInput4, 3, color4)

    print("You have " + str(correctSpot) + " correct colors in the correct spot!")
    print("You have " + str(correctColor) + " correct colors in the wrong spot!")
    
    if (correctSpot == 4):
        print("You guessed Correctly!")
        break

if (guess == 11):
    print("Womp Womp, you didn't guess in time")

