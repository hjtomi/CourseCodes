import turtle as t
import time
from snake import Snake
from food import Food
from score import Score

# GAME SETUP
screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
# We need to turn the animations off so that we can achieve a certain thing later on *
screen.tracer(0)

# Initialize the snake object
snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkeypress(snake.up, "w")
screen.onkeypress(snake.down, "s")
screen.onkeypress(snake.left, "a")
screen.onkeypress(snake.right, "d")

is_game_on = True
while is_game_on:
    # * Updates the screen only after each snake segment moved to their correct position
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < snake.segment_size:
        food.refresh()
        snake.extend()
        score.increment_score()

    # Detect collision with wall
    if abs(snake.head.xcor()) > 300 - (snake.segment_size / 2) or abs(snake.head.ycor()) > 300 - (snake.segment_size / 2):
        food.refresh()
        snake.die()
        snake = Snake()

        # update listenings
        screen.onkeypress(snake.up, "w")
        screen.onkeypress(snake.down, "s")
        screen.onkeypress(snake.left, "a")
        screen.onkeypress(snake.right, "d")

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < snake.segment_size / 2:
            food.refresh()
            snake.die()
            snake = Snake()

            # update listenings
            screen.onkeypress(snake.up, "w")
            screen.onkeypress(snake.down, "s")
            screen.onkeypress(snake.left, "a")
            screen.onkeypress(snake.right, "d")

screen.exitonclick()
