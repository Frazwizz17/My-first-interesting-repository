from turtle import Turtle
positions=[(0,0),(-20,0),(-40,0)]
move_distance=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments=[]
        self.createsnake()
        self.move()

    def createsnake(self):
        for position in positions:
            self.add_segments(position)


    def add_segments(self,position):
        timmy = Turtle()
        timmy.shape("square")
        timmy.color("white")
        timmy.penup()
        timmy.goto(position)
        self.segments.append(timmy)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.createsnake()

    def extend(self):
        self.add_segments(self.segments[-1].position())


    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(move_distance)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)









