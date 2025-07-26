
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
my_screen=Screen()
my_screen.setup(600,600)
my_screen.bgcolor("Black")
my_screen.title("Feed the Snake")
my_screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=ScoreBoard()

my_screen.listen()
my_screen.onkey(snake.up,"Up")
my_screen.onkey(snake.down,"Down")
my_screen.onkey(snake.left,"Left")
my_screen.onkey(snake.right,"Right")

game_is_on=True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 10:
        food.refresh()
        snake.extend()
        scoreboard.add_score()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -280:
        scoreboard.reset()
        snake.reset()
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            scoreboard.reset()
            snake.reset()



my_screen.exitonclick()