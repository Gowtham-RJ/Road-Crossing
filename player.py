from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 260


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pencolor("white")
        self.penup()
        self.goto(-300, 260)
        self.pendown()
        self.goto(300, 260)
        self.penup()
        self.goto(-300, -260)
        self.pendown()
        self.goto(300, -260)

        self.color("green")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def is_finished(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        return False
