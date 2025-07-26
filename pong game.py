from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score
my_screen=Screen()
my_screen.setup(800,600)
my_screen.bgcolor("black")
my_screen.title("PONG GAME!")
my_screen.tracer(0)

l_paddle=Paddle((-350,0))
r_paddle=Paddle((350,0))

my_screen.listen()
my_screen.onkey(r_paddle.go_up,"Up")
my_screen.onkey(r_paddle.go_down,"Down")
my_screen.onkey(l_paddle.go_up,"w")
my_screen.onkey(l_paddle.go_down,"s")

ball=Ball()
score=Score()

game_is_on=True
while game_is_on:
    my_screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() ==280 or ball.ycor() == -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()


    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    if ball.xcor() > 400:
        ball.refresh()
        score.l_point()

    if ball.xcor() < -400:
        ball.refresh()
        score.r_point()






my_screen.exitonclick()