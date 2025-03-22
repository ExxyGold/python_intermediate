import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


turtle = Player()
cars = CarManager()
level = Scoreboard()

screen.listen()
screen.onkey( turtle.move_turtle, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()

    cars.move_car()

    

    if turtle.finish_line():
        turtle.start_over()
        cars.speed_up()
        level.increase_score()

    for spec in cars.cars:
        if spec.distance(turtle) < 20:
            game_is_on = False
            level.game_over()

    

screen.exitonclick()