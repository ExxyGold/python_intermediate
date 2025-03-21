from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score_board import Score

screen = Screen()

screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

score = Score()
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

ball = Ball()






screen.listen()

screen.onkey( l_paddle.upward, "w" )
screen.onkey(l_paddle.downward, "s")
screen.onkey( r_paddle.upward, "Up" )
screen.onkey(r_paddle.downward, "Down")


game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() >280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor()> 325 or ball.distance(l_paddle) < 50 and ball.xcor() < -325:
        ball.ped_bounce()

    if ball.xcor() > 390:
        ball.clear()
        ball.reset_ball()
        ball.move_speed = 0.05
        score.increase_l()
        
        
    if ball.xcor() < -390:
        ball.clear()
        ball.reset_ball()
        ball.move_speed = 0.1
        score.increase_r()

        # ball.move()
        




#MOtion of ball

#Using botton to move bar

#system contolling the other bar


screen.exitonclick()