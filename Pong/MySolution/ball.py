import random
from turtle import Turtle

SPEED = 0.3


class Ball:
    def __init__(self):
        self.speed = SPEED
        self.ball = self.create_ball()

    def create_ball(self):
        ball = Turtle("circle")
        ball.color("white")
        ball.penup()
        return ball

    def set_facing(self):
        sides = {1: [135, 180], 2: [0, 45], 3: [180, 225], 4: [315, 359]}
        random_side = random.randint(1, 4)
        random_degree = random.randint(sides[random_side][0], sides[random_side][1])
        self.ball.setheading(random_degree)

    def move(self):
        self.ball.forward(self.speed)
