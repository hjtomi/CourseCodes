from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.paddle = self.create_paddle()

    def create_paddle(self):
        paddle = Turtle("square")
        paddle.shapesize(stretch_len=4)
        paddle.setheading(90)
        paddle.fillcolor("white")
        paddle.goto(-370, 0)
        return paddle
