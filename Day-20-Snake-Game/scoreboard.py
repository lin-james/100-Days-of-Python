from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.score = 0
        self.color("white")
        self.write(f"Score: {self.score}", align="center", font="Arial")

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font="Arial")

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font="Arial")
