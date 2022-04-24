from turtle import Turtle, Screen
import random
timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.pensize(1)
timmy.speed(10)
screen = Screen()
screen.bgcolor("pink")


def random_walk():
    heading = random.choice([0, 90, 180, 270])
    color = random.choice(['red', 'blue', 'green'])
    timmy.seth(heading)
    timmy.pencolor(color)
    timmy.forward(50)


def dash(s_length, num_dash):
    for step in range(num_dash):
        timmy.forward(s_length)
        timmy.penup()
        timmy.forward(s_length)
        timmy.pendown()


def draw_shape():
    for sides in range(2, 11):
        angle = 360 / sides
        for _ in range(sides):
            timmy.forward(100)
            timmy.right(angle)


def draw_spiro():
    for turn in range(0, 351, 10):
        timmy.seth(turn)
        timmy.circle(100)

# dash(10, 15)


# draw_shape()
# while True:
#     random_walk()
draw_spiro()
# timmy.circle(100)
screen.exitonclick()
