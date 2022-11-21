from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

# half line setup
half_line_turtle = Turtle()
half_line_turtle.hideturtle()
half_line_turtle.goto(0, 300)
half_line_turtle.setheading(270)
half_line_turtle.pensize(10)
half_line_turtle.color("white")

while half_line_turtle.ycor() > -300:
    half_line_turtle.forward(20)
    half_line_turtle.penup()
    half_line_turtle.forward(20)
    half_line_turtle.pendown()


screen.listen()

player = Paddle(is_ai=False)
ai = Paddle(is_ai=True)
ball = Ball()

ball.set_facing()


is_game_on = True
while is_game_on:
    screen.update()

    ball.move()

    screen.onkeypress(player.move_up_pressed, "w")
    screen.onkey(player.move_up_let, "w")

    screen.onkeypress(player.move_down_pressed, "s")
    screen.onkey(player.move_down_let, "s")

    if player.move_up and player.paddle.ycor() < 300:
        player.up()

    if player.move_down and player.paddle.ycor() > -300:
        player.down()









screen.exitonclick()

