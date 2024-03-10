import time
from turtle import *
turtle = Turtle()

def clockFace():
    turtle.speed(200)
    turtle.penup()
    turtle.width(1)
    turtle.pencolor('black')
    turtle.goto(0,0)
    turtle.pendown()
    turtle.seth(0)
    turtle.circle(100)
    for i in range(12):
        turtle.penup()
        turtle.goto(0,100)
        turtle.forward(40)
        turtle.pendown()
        if (i%3 == 0):
            turtle.width(2)
            turtle.forward(40)
        else: 
            turtle.width(1.2)
            turtle.forward(40)
        turtle.right(30)
    turtle.penup()        
    turtle.goto(0,100)
    turtle.left(90)
    for i in range(60):
        turtle.width(1)
        turtle.penup()
        turtle.goto(0,100)
        turtle.forward(70)
        turtle.pendown()
        turtle.forward(10)
        turtle.right(6)
        turtle.penup()
    turtle.goto(0,100)

currFullTime = time.ctime()
currHour = currFullTime[11] + currFullTime [12]
currMin = currFullTime[14] + currFullTime[15]
currSec = currFullTime[17] + currFullTime[18]



def minHand():
    turtle.speed(10)
    turtle.goto(0, 100)
    minDeg = int(currMin) * 6
    turtle.right(minDeg)
    turtle.backward(13)
    turtle.color('black')
    turtle.pendown()
    turtle.width(4)
    turtle.forward(93)
    turtle.goto(0,100)
    turtle.left(minDeg)

def hourHand():
    turtle.speed(10)
    turtle.goto(0, 100)
    minDeg = int(currMin) 
    hourDeg = int(currHour) * 30 + minDeg/2
    turtle.right(hourDeg)
    turtle.color('black')
    turtle.pendown()
    turtle.width(4)
    turtle.backward(13)
    turtle.forward(68)
    turtle.goto(0,100)
    turtle.left(hourDeg)

def secHand():
    turtle.speed(10)
    turtle.goto(0, 100)
    secDeg = int(currSec) * 6
    turtle.right(secDeg)
    turtle.backward(13)
    turtle.color('red')
    turtle.pendown()
    turtle.width(4)
    turtle.forward(93)
    turtle.goto(0,100)
    turtle.left(secDeg)



turtle.clear()
clockFace()
inputNum = input("Please input the number of seconds you want this to run: ")
print(currHour + ":" + currMin + ":" + currSec)
minHand()
hourHand()
for numSec in range(int(inputNum)):
    currFullTime = time.ctime()
    currSec = currFullTime[17] + currFullTime[18]
    secHand()
    time.sleep(0.5)
    for i in range(8):
        turtle.undo()


turtle.hideturtle()
time.sleep(1)