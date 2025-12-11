import turtle

screen = turtle.Screen()
screen.setup(width=400, height=300)
screen.title("Elesoper")
turtle_pixel = turtle.Turtle()
turtle_pixel.speed(1)

def design(x, y, color, pixel size):
    turtle_pixel.penup()
    turtle_pixel.goto(x, y)
    turtle_pixel.pendown()
    turtle_pixel.fillcolor(color)
    turtle_pixel.begin_fill()
    for b in range(4):
        turtle_pixel.forward(3)