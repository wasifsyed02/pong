from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,postition):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.color("white")
        self.goto(postition)

    def up(self):
        new_y=self.ycor()+20;
        self.goto(self.xcor(),new_y)
    def down(self):
        new_y=self.ycor()-20;
        self.goto(self.xcor(),new_y)
