from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import Score

screen = Screen()


screen.setup(width = 600, height= 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


food = Food()
snake = Snake()
score = Score()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

motion = True

while motion:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Check collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase()
        snake.extend()

    #Detect collision with wall

    if snake.head.xcor() > 280 or snake.head.xcor()< -280 or snake.head.ycor() > 280 or snake.head.ycor()< -280:
        motion = False
        score.game_over()
    for segment in snake.snake[1:]:
        if snake.head.distance(segment)< 10:
            motion = False
            score.game_over()



screen.exitonclick()