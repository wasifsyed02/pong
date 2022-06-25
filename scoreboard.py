from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.draw()
    def draw(self):
        self.clear()
        self.goto(-100,195)
        self.write(self.l_score,align="center",font=("alrial",80,"normal"))
        self.goto(100,195)
        self.write(self.r_score,align="center",font=("alrial",80,"normal"))

    def increae_l_score(self):
        self.l_score+=1
    def increae_r_score(self):
        self.r_score+=1