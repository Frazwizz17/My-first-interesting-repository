from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1.2,1.2)
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.new_x = 10
        self.new_y = 10
        self.move_speed = 0.1

    def move(self):
        new_xcor = self.xcor() + self.new_x
        new_ycor = self.ycor() + self.new_y
        self.goto(new_xcor,new_ycor)

    def bounce_y(self):
        self.new_y*=-1


    def bounce_x(self):
        self.new_x*=-1
        self.move_speed*=0.9

    def refresh(self):
        self.goto(0,0)
        self.move_speed=0.1
        self.bounce_x()




