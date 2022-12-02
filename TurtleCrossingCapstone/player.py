from turtle import Turtle

SPEED = 1.5


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.stage_start()

    def stage_start(self):
        self.goto(0, -270)

    def move(self):
        self.forward(SPEED)
