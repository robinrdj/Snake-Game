from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()
    # Detect collision with food
    if snake.segments[0].distance(food) < 30:
        food.refresh()
        scoreboard.increase_score()
        snake.add_segment()
    # Detect collision with wall
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() <-280 or snake.segments[0].ycor() >280 or snake.segments[0].ycor() < -280:
        snake.reset_snake()
        scoreboard.reset()

    # Detect collision with tail
    # if head collides with anyone of the segments
    for seg in snake.segments[1:]:

        if snake.segments[0].distance(seg) < 10:
            snake.reset_snake()
            scoreboard.reset()







screen.exitonclick()


















screen.exitonclick()