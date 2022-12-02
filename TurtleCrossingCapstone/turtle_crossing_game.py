from turtle import Screen, colormode
from player import Player
from car import Car
from stage import Stage
import time

iterations_without_new_car = 30
cars = []
car_speed = 2
w_down = False
def w_down_true():
    global w_down
    w_down = True
def w_down_false():
    global w_down
    w_down = False


screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.listen()
colormode(255)

player = Player()
stage = Stage()

iterations = 0
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.01)
    iterations += 1

    # Detect w key
    screen.onkeypress(w_down_true, "w")
    screen.onkey(w_down_false, "w")

    # Move turtle if w_down is True
    if w_down:
        player.move()

    # Create new car
    if iterations > iterations_without_new_car:
        iterations = 0
        cars.append(Car(car_speed))

    # Move cars
    for car in cars:
        car.move()

    # Remove car that left the scree
    # logic: we only check the first car in list and remove that, because it's always the first
    if cars:
        if cars[0].xcor() < -350:
            cars.pop(0)

    # COLLISIONS
    # Detect finish
    if player.ycor() > 280:
        stage.stage_up()
        player.stage_start()
        for car in cars:
            car.hideturtle()
        cars.clear()
        car_speed *= 1.2
        iterations_without_new_car *= 0.8

    # Detect collision with car
    for car in cars:
        if car.distance(player) < 20:
            # Game over
            stage.game_over()
            is_game_on = False

screen.exitonclick()
