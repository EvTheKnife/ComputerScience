from turtle import *
import time
turtle = Turtle()
screen = Screen()

screen.bgcolor(0, 0, 0)
colors = ['red', 'orange', 'yellow', 'green', 'blue',  'violet']
turtle.speed(100)

def circles():
    turtle.goto(-175, 0)
    for circleNum in range(12):
        turtle.color(colors[circleNum%6])
        turtle.penup()
        turtle.width(20)
        turtle.pendown()
        turtle.circle(50)
        turtle.penup()
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(10)
        turtle.right(90)
    for circleNum in range(18):
        turtle.color(colors[circleNum%6])
        turtle.penup()
        turtle.width(20)
        turtle.pendown()
        turtle.circle(50)
        turtle.forward(10)
    for circleNum in range(12):
        turtle.color(colors[circleNum%6])
        turtle.penup()
        turtle.width(20)
        turtle.pendown()
        turtle.circle(50)
        turtle.penup()
        turtle.forward(10)
        turtle.right(90)
        turtle.forward(10)
        turtle.left(90)
def petalThingy():
    for petalNum in range(12):
        turtle.penup()
        turtle.goto(30,0)
        turtle.color(colors[petalNum%6])
        turtle.width(1)
        turtle.pendown()
        turtle.circle(50)
        turtle.left(30)

circles()
petalThingy()

time.sleep(2)

