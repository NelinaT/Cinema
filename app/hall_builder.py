import turtle

row_names = ["A","B", "C","D","E","F","G","H","I","J"]

t = t = turtle.Turtle()
t.hideturtle()

for i in range(0,5):
    for j in range(0,5):
        t.goto(i*70,j*70)
        t.pendown()
        t.pen(pencolor="black", fillcolor="green", pensize= 1, speed=0)
        print(t.pos())
        t.begin_fill()
        t.forward(50) 
        t.left(90)
        t.forward(50) 
        t.left(90)
        t.forward(50) 
        t.left(90)
        t.forward(50) 
        t.left(90)
        t.end_fill()
        t.penup()
        t.goto(i*70 + 25 ,j*70 +10)
        t.write(f"{row_names[j]}" + f'{i+1}', align="center", font=('Arial', 15, 'normal'))
t.pen(fillcolor = "blue", pensize= 2)
t.begin_fill()
t.goto(-20,-90)
t.forward(370) 
t.left(90)
t.forward(50) # Forward turtle by s units
t.left(90) # Turn turtle by 90 degree
t.forward(370) # Forward turtle by s units
t.left(90) # Turn turtle by 90 degree
t.forward(50) # Forward turtle by s units
t.left(90) # Turn turtle by 90 degree
t.end_fill()
t.goto(180 ,-75)
t.write("SCREEN", align="center", font=('Arial', 15, 'normal'))


turtle.done()


# ****************************************************************************************
# t = turtle.getscreen()

# t1 = turtle.Turtle(shape='circle')

# t = turtle.Turtle()
# t.hideturtle()

# for i in range(0,5):
#     for j in range(0,5):
#         t.goto(i*100,j*100)
#         t.pendown()
#         t.pen(pencolor="black", fillcolor="green", pensize= 5, speed=0)
#         print(t.pos())
#         t.begin_fill()
#         t.write("55", align="center", font=('Arial', 20, 'normal'))
#         t.circle(30)
#         t.end_fill()
#         t.penup()

# t.pen(fillcolor = "blue", pensize= 2)
# t.begin_fill()
# t.goto(-60,-60)
# t.forward(500) 
# t.left(90)
# t.forward(50) # Forward turtle by s units
# t.left(90) # Turn turtle by 90 degree
# t.forward(500) # Forward turtle by s units
# t.left(90) # Turn turtle by 90 degree
# t.forward(50) # Forward turtle by s units
# t.left(90) # Turn turtle by 90 degree
# t.end_fill()
# turtle.done()
# **************************************************************************************************************

# from svg_turtle import SvgTurtle


# def draw_spiral(t):
#     # t1 = turtle.Turtle(shape='circle')

#     # t = turtle.Turtle()
#     t.hideturtle()

#     for i in range(0,5):
#         for j in range(0,5):
#             t.goto(i*100,j*100)
#             t.pendown()
#             t.pen(pencolor="black", fillcolor="green", pensize= 5, speed=0)
#             print(t.pos())
#             t.begin_fill()
#             t.write("55", align="center", font=('Arial', 20, 'normal'))
#             t.circle(30)
#             t.end_fill()
#             t.penup()

#     t.pen(fillcolor = "blue", pensize= 2)
#     t.begin_fill()
#     t.goto(-60,-60)
#     t.forward(500) 
#     t.left(90)
#     t.forward(50) # Forward turtle by s units
#     t.left(90) # Turn turtle by 90 degree
#     t.forward(500) # Forward turtle by s units
#     t.left(90) # Turn turtle by 90 degree
#     t.forward(50) # Forward turtle by s units
#     t.left(90) # Turn turtle by 90 degree
#     t.end_fill()

#     # turtle.done()


# def write_file(draw_func, filename, width, height):
#     t = SvgTurtle(width, height)
#     draw_func(t)
#     t.save_as(filename)


# def main():
#     write_file(draw_spiral, 'example.svg', 1500, 1500)
#     print('Done.')


# if __name__ == '__main__':
#     main()