from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
# screen.bgcolor("black")
screen.tracer(0)

halflinet = Turtle()
halflinet.color("white")
halflinet.penup()
halflinet.goto(0, 300)
halflinet.pendown()
halflinet.setheading(270)

while halflinet.ycor() < -300:
    halflinet.forward(20)
    halflinet.penup()
    halflinet.forward(20)
    halflinet.pendown()

player = Paddle()



screen.update()












screen.exitonclick()

