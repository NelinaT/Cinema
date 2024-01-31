from svg_turtle import SvgTurtle
import turtle

row_names = ["A","B", "C","D","E","F","G","H","I","J"]

def parallelogram(width, height,t):
    for _ in range(2):
        t.forward(width) 
        t.left(90)
        t.forward(height) 
        t.left(90)

def grid_of_seats(cols,rows, seat_width,t):
    t.hideturtle()
    t.penup()

    for col in range(cols):
        for row in range(rows):
            t.goto(-300 + col*70, -200 + row*70)
            t.pendown()
            t.pen(pencolor="black", fillcolor="green", pensize= 1, speed=0)
            t.begin_fill()
            parallelogram(seat_width,seat_width,t)
            t.end_fill()
            t.penup()
            t.goto(-300+col*70 + 25 ,-200 + row*70 +10)
            t.write(f"{row_names[row]}" + f'{col+1}', align="center", font=('Arial', 15, 'normal'))

    t.pen(fillcolor = "black", pensize= 2)
    t.begin_fill()
    t.goto(-320,-290)
    screen_lenght = cols *( seat_width + 25)
    parallelogram(screen_lenght,50,t)
    t.end_fill()
    t.goto(-300+cols*36 ,-275)
    t.color('white')
    t.write("SCREEN", align="center", font=('Arial', 15, 'normal'))
    # turtle.done()


# t=turtle.Turtle()
# grid_of_seats(10,10,50,t)



def generate_svg(filename, width, height,rows, cols):
    t = SvgTurtle(width, height)
    grid_of_seats(cols,rows,50,t)
    t.save_as(filename)
    return filename


# def generate_svg():
#     write_file(grid_of_seats, 'example.svg', 1500, 1500)
#     print('Done.')
    


# generate_svg()

# generate_svg(grid_of_seats, 'app/static/app/example.svg', 1500, 1500,3,4 )