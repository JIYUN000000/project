from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.direction = "Stop"
        self.head = self.segments[0]

    def create_snake(self):
            for position in STARTING_POSITION:
                self.add_segment(position)


    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        # add a new segment to the snake
        self.add_segment(self.segments[-1].position())

    def move(self):


        for seg_num in range(len(self.segments) - 1, 0, -1):  # from 3-1 = 2 to 0, with step -1
            new_x = self.segments[ seg_num - 1].xcor()  # from 2-1 = 1. following x of segments[1] -next step-> following x of segments[0]
            new_y = self.segments[seg_num - 1].ycor()  # following y of segments[1] -next step -> following y of segments[1]
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
          self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


