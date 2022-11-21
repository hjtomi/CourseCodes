from turtle import Turtle
SPEED = 0.5


class Paddle(Turtle):
    def __init__(self, is_ai):
        super().__init__()
        self.is_ai = is_ai
        self.speed = SPEED
        self.move_up = False
        self.move_down = False
        self.shape("square")
        self.shapesize(stretch_len=4)
        self.setheading(90)
        self.color("white")
        self.penup()
        if self.is_ai:
            self.goto(370, 0)
        else:
            self.goto(-370, 0)

    def up(self):
        self.forward(self.speed)

    def down(self):
        self.back(self.speed)

    def move_up_pressed(self):
        self.move_up = True

    def move_up_let(self):
        self.move_up = False

    def move_down_pressed(self):
        self.move_down = True

    def move_down_let(self):
        self.move_down = False


