from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 280)

        with open("Day-20-Snake-Game\data.txt") as file:
            self.highscore = int(file.read())
        print(f"{self.highscore}")
        self.score = 0
        self.color("white")
        self.write(
            f"Score: {self.score} Highscore: {self.highscore}", align="center", font="Arial")

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} Highscore: {self.highscore}", align="center", font="Arial")

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("Day-20-Snake-Game\data.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()
