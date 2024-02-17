from svg_turtle import SvgTurtle
from . utils import row_names_dict


def is_seat_available(seat, tickets):
    
    for ticket in tickets:
        if ticket.seat == seat:
            return False
    return True

def parallelogram(width, height,t):
    for _ in range(2):
        t.forward(width) 
        t.left(90)
        t.forward(height) 
        t.left(90)

def grid_of_seats(seat_width,t,seats, tickets, cols):
    t.hideturtle()
    t.penup()

    for seat in seats:
        t.goto(-300 + (seat.col-1)*70, -200 + row_names_dict[seat.row]*70)
        t.pendown()
        if not seat.is_available:
            t.pen(pencolor="black", fillcolor="red", pensize= 1, speed=0)
        elif is_seat_available(seat, tickets):
            t.pen(pencolor="black", fillcolor="green", pensize= 1, speed=0)
        else:
            t.pen(pencolor="black", fillcolor="gray", pensize= 1, speed=0)
            
        t.begin_fill()
        parallelogram(seat_width,seat_width,t)
        t.end_fill()
        t.penup()
        t.goto(-300+(seat.col-1)*70 + 25 ,-200 + row_names_dict[seat.row]*70 +10)
        t.write(f"{seat.row}" + f'{seat.col}', align="center", font=('Arial', 15, 'normal'))

    t.pen(fillcolor = "black", pensize= 2)
    t.begin_fill()
    t.goto(-320,-290)
    screen_lenght = cols *( seat_width + 25)
    parallelogram(screen_lenght,50,t)
    t.end_fill()
    t.goto(-300+cols*36 ,-275)
    t.color('white')
    t.write("SCREEN", align="center", font=('Arial', 15, 'normal'))

def generate_svg(filename, width, height, seats, tickets, cols):
    t = SvgTurtle(width, height)
    grid_of_seats(50,t,seats,tickets,cols)
    t.save_as(filename)
    return filename