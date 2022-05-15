import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
screen.listen()
screen.onkey(player.move, "d")
screen.onkey(player.move, "f")
screen.onkey(player.move, "j")
screen.onkey(player.move, "k")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move(scoreboard.level)
    # if player reaches finish line
    if player.ycor() >= FINISH_LINE_Y:
        scoreboard.inc_score()
        player.reset_pos()

    # if player collides with car
    for car in car_manager.all_cars:
        if player.distance(car.xcor(), car.ycor()) < 30:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
