import random
import turtle

colors = [(207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203)]
tim = turtle.Turtle()
turtle.colormode(255)

tim.speed(0)
tim.pensize(20)
tim.penup()

ypos = -300
tim.setpos(-200, ypos)
def draw_hirst(x, y, ypos):
    for i in range(y):
        tim.setpos(-300, ypos)
        for i in range(x):
            tim.dot(30, random.choice(colors))
            tim.forward(40)

        ypos += 50


draw_hirst(20, 20, ypos)

my_screen = turtle.Screen()
my_screen.exitonclick()
