from turtle import Turtle

START = [(0,0),(-20,0),(-40,0)]
FORWARD_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
    def create_snake(self):
        for x in START:  
            self.add(x)
    def add(self, position):
        a = Turtle("square")
        a.color("white")
        a.penup()
        a.goto(position)
        self.segment.append(a)
    def extend(self):
        self.add(self.segment[-1].position())
    def move(self):
        for x in range(len(self.segment)-1, 0, -1):
            u = self.segment[x-1].xcor()
            v = self.segment[x-1].ycor()
            z = self.segment[x]
            z.goto(u, v)
        self.head.forward(FORWARD_DISTANCE)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            print("up")
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

