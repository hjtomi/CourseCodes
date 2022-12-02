from turtle import Turtle
import random

MAX_Y = 280
MIN_Y = -240


class Car(Turtle):
    def __init__(self, move_speed):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=2.2)
        self.set_random_color()
        self.setheading(180)
        self.set_random_y()

        self.move_speed = move_speed

    def set_random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        col = (r, g, b)
        self.color(col)

    def set_random_y(self):
        y = random.randint(MIN_Y, MAX_Y)
        self.goto(350, y)

    def move(self):
        self.forward(self.move_speed)

