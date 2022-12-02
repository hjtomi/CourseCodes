import turtle as t
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP_ANGLE = 90
DOWN_ANGLE = 270
LEFT_ANGLE = 180
RIGHT_ANGLE = 0

# Extra options
SIZE_MULTIPLIER = 1  # MOVE_DISTANCE / SIZE_MULTIPLIER ration: 20 : 1
EXTEND_LENGTH = 1


class Snake:
    def __init__(self):
        self.segments = []
        self.facing = 0
        self.segment_size = 20 * SIZE_MULTIPLIER
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # We create 3 block as the starting snake
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = t.Turtle("square")
        # Default pixel size of square: 20x20
        new_segment.shapesize(SIZE_MULTIPLIER, SIZE_MULTIPLIER)
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)

        self.segments.append(new_segment)

    def die(self):
        for segment in self.segments:
            segment.goto(1000, 1000)

    # LOGIC:
    # The extension of the snake is just adding an extra square on top of the last one
    # So the next move cycle each square excluding the one added moves ahead
    # On the next move cycle the snake is longer
    def extend(self):
        for _ in range(EXTEND_LENGTH):
            self.add_segment(self.segments[-1].position())

    def move(self):
        # So the logic is to move the last segment to the one ahead of it, then the next to the one ahead of it and so on...
        # once we moved all the segments, the first square can move forward
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

        self.facing = int(self.segments[0].heading())

    def up(self):
        if self.facing != DOWN_ANGLE:
            self.head.setheading(UP_ANGLE)

    def down(self):
        if self.facing != UP_ANGLE:
            self.head.setheading(DOWN_ANGLE)

    def left(self):
        if self.facing != RIGHT_ANGLE:
            self.head.setheading(LEFT_ANGLE)

    def right(self):
        if self.facing != LEFT_ANGLE:
            self.head.setheading(RIGHT_ANGLE)

