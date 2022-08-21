from turtle import Turtle

SNAKE_SEGMENTS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_body()
        self.face = self.segments[0]

    def create_body(self):
        for parts in SNAKE_SEGMENTS:
            snake_body = Turtle(shape='square')
            snake_body.penup()
            snake_body.color('green')
            snake_body.goto(parts)
            self.segments.append(snake_body)

    def move(self):
        for snake in range(len(self.segments) - 1, 0, -1):
            xo = self.segments[snake - 1].xcor()
            yo = self.segments[snake - 1].ycor()
            self.segments[snake].goto(x=xo, y=yo)

        self.face.forward(MOVE_DIS)

    def up(self):
        if self.face.heading() != DOWN:
            self.face.setheading(UP)

    def down(self):
        if self.face.heading() != UP:
            self.face.setheading(DOWN)

    def left(self):
        if self.face.heading() != RIGHT:
            self.face.setheading(LEFT)

    def right(self):
        if self.face.heading() != LEFT:
            self.face.setheading(RIGHT)
