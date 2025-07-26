from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.8)
        self.color("blue")
        self.penup()
        self.speed(0)
        self.refresh()


    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
