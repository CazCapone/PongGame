from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0
        self.update_score()

    def p1_point(self):
        self.p1_score += 1
        self.update_score()

    def p2_point(self):
        self.p2_score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.p1_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.p2_score, align=ALIGNMENT, font=FONT)
