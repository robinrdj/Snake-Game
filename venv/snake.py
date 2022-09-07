STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
from turtle import Turtle
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):

        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def add_segment(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        seg_x = self.segments[len(self.segments) - 1].xcor()
        seg_y = self.segments[len(self.segments) - 1].ycor()
        new_segment.goto(seg_x, seg_y)
        self.segments.append(new_segment)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            seg_x = self.segments[seg - 1].xcor()
            seg_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(seg_x, seg_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()



    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right (self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT) 












