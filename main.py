from turtle import Turtle,Screen
import time

from scoreboard import ScoreBoard
#creating screen object
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
# screen.tracer(0)

#createing turtle
from paddle import Paddle
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
#creating a ball 
from ball import Ball
ball=Ball()
#creating score board
from scoreboard import ScoreBoard
scoreboard=ScoreBoard()
#drawing a line on board.
from line import Line
divider=Line()

#listning when any key is pressed.
screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")
game_is_on=True
while game_is_on:
    time.sleep(ball.speed)
    screen.update()
    ball.move()
    #checking if ball hits wall
    if(ball.ycor()>280 or ball.ycor()<-280):
        ball.bounce_y()
    # checking of ball hits right or left paddle.
    if(ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320):
        ball.speed_up()
        ball.bounce_x()
    #checking if right paddle misses the ball  
    if(ball.xcor()>380):
        scoreboard.increae_l_score()
        scoreboard.draw()
        ball.reset()
    #checking if left paddle misses the ball 
    if(ball.xcor()<-380):
        scoreboard.increae_r_score()
        scoreboard.draw()
        ball.reset()

screen.exitonclick()