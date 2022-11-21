import turtle
import random

tim = turtle.Turtle()
tim.color("dark green")
tim.speed(0)
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.circle(150)
        tim.left(size_of_gap)
        tim.color(random_color())


draw_spirograph(2)

my_screen = turtle.Screen()
my_screen.exitonclick()
