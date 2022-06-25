from turtle import Turtle
class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0,-300)
        self.hideturtle()
        self.left(90)
        for i in range(100):
            self.dot()
            self.forward(10)
        