from turtle import Turtle
SPEED = 0.1


class Paddle:
    def __init__(self, is_ai):
        self.is_ai = is_ai
        self.speed = SPEED
        self.paddle = self.create_paddle()
        self.move_up = False
        self.move_down = False

    def create_paddle(self):
        paddle = Turtle("square")
        paddle.shapesize(stretch_len=4)
        paddle.setheading(90)
        paddle.color("white")
        paddle.penup()
        if self.is_ai:
            paddle.goto(370, 0)
        else:
            paddle.goto(-370, 0)
        return paddle

    def up(self):
        self.paddle.forward(self.speed)

    def down(self):
        self.paddle.back(self.speed)

    def move_up_pressed(self):
        self.move_up = True

    def move_up_let(self):
        self.move_up = False

    def move_down_pressed(self):
        self.move_down = True

    def move_down_let(self):
        self.move_down = False


