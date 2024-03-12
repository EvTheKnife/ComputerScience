from turtle import *
turtle = Turtle()

def gameBoard():
    turtle.penup()
    turtle.goto(-20, 60)
    turtle.pendown()
    turtle.goto(-20, -60)
    turtle.penup()
    turtle.goto(20, -60)
    turtle.pendown()
    turtle.goto(20,60)
    turtle.penup()
    turtle.goto(60,60)
    turtle.goto(60, 20)
    turtle.pendown()
    turtle.goto(-60, 20)
    turtle.penup()
    turtle.goto(-60, -20)
    turtle.pendown()
    turtle.goto(60, -20)

def drawX():
    pass

def drawO():
    pass

gameBoard()