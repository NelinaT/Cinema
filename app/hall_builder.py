import turtle
import tkinter
from svg_turtle import SvgTurtle

t1 = turtle.Turtle(shape='circle')

t = turtle.Turtle()
t.hideturtle()

for i in range(0,5):
    for j in range(0,5):
        t.goto(i*100,j*100)
        t.pendown()
        t.pen(pencolor="black", fillcolor="green", pensize= 5, speed=0)
        print(t.pos())
        t.begin_fill()
        t.write("55", align="center", font=('Arial', 20, 'normal'))
        t.circle(30)
        t.end_fill()
        t.penup()

t.pen(fillcolor = "blue", pensize= 2)
t.begin_fill()
t.goto(-60,-60)
t.forward(500) 
t.left(90)
t.forward(50) # Forward turtle by s units
t.left(90) # Turn turtle by 90 degree
t.forward(500) # Forward turtle by s units
t.left(90) # Turn turtle by 90 degree
t.forward(50) # Forward turtle by s units
t.left(90) # Turn turtle by 90 degree
t.end_fill()



turtle.done()