from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=800, height=800)


turtle_list = []
turtle_color = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
turtle_index = [-60, -40, -20, 0, 20, 40, 60]
for i in range(0, len(turtle_color)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_color[i])
    turtle_list.append(new_turtle)
    new_turtle.penup()
    new_turtle.goto(-390, turtle_index[i])

bet = screen.textinput(title="Betting Window", prompt="Who?")


is_race_on = True
while is_race_on:

    for i in turtle_list:
        step = random.randint(1, 10)
        i.forward(step)
        if i.xcor() > 390 and i.pencolor() == bet:
            is_race_on = False
            print(f"You won")
        elif i.xcor() > 390 and i.pencolor() != bet:
            is_race_on = False
            print(f"You lost")
        else:
            pass
            # winner = i.pencolor()


# if winner == bet:
#     print(f"You won! {winner} won the race!")
# else:
#     print(f"You lost! {winner} won the race!")
screen.exitonclick()
