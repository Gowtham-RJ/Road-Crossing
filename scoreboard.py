from turtle import Turtle

FONT = ("Courier", 24, "bold")
FONT2 = ("Courier", 30, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-290, 260)
        self.write(arg=f"Level: {self.level}", font=FONT, align="left")

    def upgrade_score(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level: {self.level}", font=FONT, align="left")

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER!", font=FONT2, align="center")
