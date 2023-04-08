from turtle import Turtle

COORDINATES = [(0, 0), (-10, 0), (-20, 0)]
SIZE = 10
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.color('silver')

    def create_snake(self):
        for coordinate in COORDINATES:
            self.add_segment(coordinate)

    def add_segment(self, coordinate):
        new_square = Turtle(shape='square')
        new_square.penup()
        new_square.color('white')
        new_square.goto(coordinate)
        new_square.turtlesize(stretch_len=0.5, stretch_wid=0.5)
        self.segments.append(new_square)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto((new_x, new_y))
        self.head.forward(SIZE)

    # Controls Start

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # Controls End
