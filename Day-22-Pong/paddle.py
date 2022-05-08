from turtle import Turtle
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)
        self.top_surface = 50
        self.bot_surface = -50

    def up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor()+10)
            self.top_surface += 10
            self.bot_surface += 10

    def down(self):
        if self.ycor() > -250:
            self.goto(self.xcor(), self.ycor()-10)
            self.top_surface -= 10
            self.bot_surface -= 10

    def touch_surface(self, ycor):
        return ycor > self.bot_surface and ycor < self.top_surface
