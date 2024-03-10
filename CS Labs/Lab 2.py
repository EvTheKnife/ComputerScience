import time
from turtle import *
turtle = Turtle()


turtle.width(2) #sets the turtle line width
turtle.speed(20)

def headEyes():
    #draws head & eyes
    turtle.color('black')
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.circle(75)
    turtle.penup()
    turtle.goto(-30,90)
    turtle.pendown()
    turtle.circle(15)
    turtle.penup()
    turtle.goto(30,90)
    turtle.pendown()
    turtle.circle(15)

def happi():
    #draws a happy mouth
    turtle.color('black')
    turtle.penup()
    turtle.goto(-15,30)
    turtle.pendown()
    turtle.goto(-15,30)
    turtle.goto(0,20)
    turtle.goto(15,30)
def happiErase():
    #erases a happy mouth
    turtle.color('white')
    turtle.penup()
    turtle.goto(-15,30)
    turtle.pendown()
    turtle.goto(-15,30)
    turtle.goto(0,20)
    turtle.goto(15,30)

def sad():
    #draws a sad mouth
    turtle.color('black')
    turtle.penup()
    turtle.goto(-15,20)
    turtle.pendown()
    turtle.goto(0,30)
    turtle.goto(15,20)
def sadErase():
    #erases a sad mouth
    turtle.color('white')
    turtle.penup()
    turtle.goto(-15,20)
    turtle.pendown()
    turtle.goto(0,30)
    turtle.goto(15,20)

def neutral():
    #literally just draws a straight line
    turtle.color('black')
    turtle.penup()
    turtle.goto(-25,25)
    turtle.pendown()
    turtle.goto(25,25)
def neutralErase():
    #literally just erases a straight line
    turtle.color('white')
    turtle.penup()
    turtle.goto(-25,25)
    turtle.pendown()
    turtle.goto(25,25)

headEyes()
emotionQuestion = input("How are you feeling? ")

if emotionQuestion.lower() == "happy" or emotionQuestion.lower() == "good":
    #does this stuff if the user enters "happy"
    sad()
    print("I'm sorry you feel that way!") #yes it's intentional to say "I'm sorry you feel that way!" when someone feels good
    time.sleep(2)
    sadErase()

elif emotionQuestion.lower() == "sad" or emotionQuestion.lower() == "bad":
    #does this stuff if the user enters "sad"
    happi()
    print("That's Good!") #yes it's intentional to say "That's good" when someone feels bad
    time.sleep(2)
    happiErase

else:
    #does this stuff if the user doesnt enter either "happy" or "sad"
    neutral()
    print("idrc lmao")
    time.sleep(2)
    neutralErase

time.sleep(.75)

