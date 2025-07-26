
from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.new_score=0
        with open("data.txt","r") as high_Score:
            f=int(high_Score.read())
            self.high_score=f

        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.new_score}  Highest Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.new_score > self.high_score:
            self.high_score=self.new_score
            with open("data.txt","w") as high_Score:
                high_Score.write(f"{self.high_score}")
        self.new_score=0



    def add_score(self):
        self.new_score+=1
        self.update_scoreboard()



