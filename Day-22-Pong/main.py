from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


r_pad = Paddle((350, 0))
l_pad = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_pad.up, "Up")
screen.onkeypress(r_pad.down, "Down")
screen.onkeypress(l_pad.up, "w")
screen.onkeypress(l_pad.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() == 330 and r_pad.touch_surface(ball.ycor()) or ball.xcor() == -330 and l_pad.touch_surface(ball.ycor()):
        ball.bounce_x()

    if ball.xcor() > 390:
        scoreboard.l_point()
        ball.reset_pos()
    if ball.xcor() < -390:
        scoreboard.r_point()
        ball.reset_pos()
screen.exitonclick()
