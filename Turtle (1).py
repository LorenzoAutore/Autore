import turtle

screen = turtle.Screen()
screen.setup(width=400, height=300)
screen.title("Elesoper")
turtle_pixel = turtle.Turtle()
turtle_pixel.speed(1)

screen.colormode(255)

R = 255
G = 182
B = 193
screen.bgcolor(R, G, B)

turtle.turtlesize(10)

turtle_pixel.goto(-100, -100)
turtle_pixel.begin_fill()
turtle_pixel.color("black")

for i in range(4):
    turtle_pixel.forward(100)
    turtle_pixel.left(90)
turtle_pixel.end_fill()

turtle_pixel.penup()
turtle_pixel.goto(100, -100)
turtle_pixel.pendown()
turtle_pixel.begin_fill()
turtle_pixel.color("blue")

for i in range(5):
    turtle_pixel.forward(100)
    turtle_pixel.left(90)
turtle_pixel.end_fill()
