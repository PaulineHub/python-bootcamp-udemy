from turtle import Screen, Turtle
from field_cls import Field
from paddle_cls import Paddle
from ball_cls import Ball
from scoreboard_cls import Scoreboard
import time

# Parameters of the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0) #control animation of elements placing themself on screen at the begining with screen.update()

# Create field, paddles, ball, scoreboard
field = Field()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350, 0))
ball = Ball()
r_scoreboard = Scoreboard((50, 230))
l_scoreboard = Scoreboard((-50, 230))

# Direct paddle's movements
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


# Play
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with r_paddle or l_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect when r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        l_scoreboard.inscrease()

    #Detect when l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        r_scoreboard.inscrease()

# exit the screen
screen.exitonclick()
