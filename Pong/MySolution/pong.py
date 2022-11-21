import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score

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
score = Score()

ball.set_facing()


paddle_hit_detection_cooldown = 0
hit_player = hit_ai = False
is_game_on = True
while is_game_on:
    screen.update()

    ball.move()

    screen.onkeypress(player.move_up_pressed, "w")
    screen.onkey(player.move_up_let, "w")

    screen.onkeypress(player.move_down_pressed, "s")
    screen.onkey(player.move_down_let, "s")

    # Forbids the player to go off-screen
    if player.move_up and player.ycor() < 300:
        player.up()
    if player.move_down and player.ycor() > -300:
        player.down()

    # Detect ball collision with screen and bounce
    if abs(ball.ycor()) > 280:
        ball.wall_bounce()

    # Detect ball collision with paddle and bounce
    # player
    if abs(player.xcor() - ball.xcor()) <= 20 and abs(player.ycor() - ball.ycor()) <= 50:
        hit_player = True
    # ai
    elif abs(ai.xcor() - ball.xcor()) <= 20 and abs(ai.ycor() - ball.ycor()) <= 50:
        hit_ai = True
    else:
        hit_player = False
        hit_ai = False

    if 0 < paddle_hit_detection_cooldown < 1000:
        paddle_hit_detection_cooldown += 1
    else:
        paddle_hit_detection_cooldown = 0

    if (hit_player or hit_ai) and paddle_hit_detection_cooldown == 0:
        ball.paddle_bounce()
        paddle_hit_detection_cooldown = 1

    # Detect when the ball flies out
    if abs(ball.xcor()) > 420:

        if ball.xcor() < -400:
            score.ai_score += 1
        else:
            score.player_score += 1

        ball.reset_position()
        score.write_score()
        screen.update()

        time.sleep(2)





screen.exitonclick()
