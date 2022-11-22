import random
from turtle import Turtle

STARTING_SPEED = 0.4
SPEED_INCREASE = 0.05


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.move_speed = STARTING_SPEED
        self.shape("circle")
        self.color("white")
        self.penup()

    def reset_position(self):
        self.goto(0, 0)
        self.set_facing()
        self.move_speed = STARTING_SPEED

    def set_facing(self):
        sides = {1: [135, 180], 2: [0, 45], 3: [180, 225], 4: [315, 359]}
        random_side = random.randint(1, 4)
        random_degree = random.randint(sides[random_side][0], sides[random_side][1])
        self.setheading(random_degree)

    def move(self):
        self.forward(self.move_speed)

    def increase_speed(self):
        self.move_speed += SPEED_INCREASE

    def wall_bounce(self):
        # Decide where the ball should face according to where the ball is facing at the time of impact
        # NE impact
        if self.heading() < 90:
            self.setheading(360 - self.heading())

        # NW impact
        elif self.heading() < 180:
            self.setheading(180 + (180 - self.heading()))

        # SW impact
        elif self.heading() < 270:
            self.setheading(180 - (self.heading() - 180))

        # SE impact
        elif self.heading() < 360:
            self.setheading(360 - self.heading())

    def paddle_bounce(self):
        # NE impact
        if self.heading() < 90:
            self.setheading(180 - self.heading())

        # NW impact
        elif self.heading() < 180:
            self.setheading(180 - self.heading())

        # SW impact
        elif self.heading() < 270:
            self.setheading(270 + (270 - self.heading()))

        # SE impact
        elif self.heading() < 360:
            self.setheading(270 - (self.heading() - 270))

