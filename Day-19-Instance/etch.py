from turtle import Turtle, Screen


def move_forward():
    cursor.forward(10)


def move_backward():
    cursor.backward(10)


def turn_left():
    cursor.left(10)


def turn_right():
    cursor.right(10)


cursor = Turtle()
screen = Screen()

screen.listen()
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_backward, "s")
screen.onkeypress(turn_left, "a")
screen.onkeypress(turn_right, "d")
screen.exitonclick()
